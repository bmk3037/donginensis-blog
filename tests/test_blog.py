import json
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from blog import blogs, existing, generate, quality, render, topics

SAMPLE_POST = {
    "title": "지능형 제어반이란? 일반 제어반과 다른 점",
    "body_markdown": (
        "## 지능형 제어반\n\n**제어**와 데이터 수집을 함께 합니다.\n\n"
        "[사진: 제어반 내부]\n\n- 권선온도\n- 진동\n\n"
        "[자세히 보기](https://donginensis.com/manufacturing.html#inquiry)"
    ),
    "tags": ["동인엔시스", "#지능형 제어반"],
    "fact_check": ["750건 이상 프로젝트"],
}


class RenderTest(unittest.TestCase):
    def test_utm_goes_before_anchor(self):
        url = render.add_utm("https://donginensis.com/manufacturing.html#inquiry", "post001")
        self.assertEqual(
            url,
            "https://donginensis.com/manufacturing.html"
            "?utm_source=naver_blog&utm_medium=blog&utm_campaign=post001#inquiry",
        )

    def test_only_site_links_are_tagged(self):
        text = "[a](https://donginensis.com/) [b](https://example.com/x)"
        out = render.tag_site_links(text, "c")
        self.assertIn("donginensis.com/?utm_source=naver_blog", out)
        self.assertIn("https://example.com/x)", out)

    def test_html_has_inline_styles_and_photo_box(self):
        out = render.to_html(SAMPLE_POST["body_markdown"])
        self.assertIn('<h2 style="', out)
        self.assertIn('<strong style="', out)
        self.assertIn('<a style="', out)
        self.assertIn("📷 사진 넣을 자리: 제어반 내부", out)
        self.assertNotIn("[사진:", out)


class TopicsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.csv = self.tmp / "topics.csv"
        rows = [
            {"id": "1", "blog": "bmk3037", "status": "published", "category": "A", "title": "t1", "keyword": "", "landing_url": "", "brief": ""},
            {"id": "2", "blog": "bmk3037", "status": "todo", "category": "A", "title": "t2", "keyword": "", "landing_url": "", "brief": ""},
            {"id": "3", "blog": "donginensis", "status": "todo", "category": "A", "title": "t3", "keyword": "", "landing_url": "", "brief": ""},
            {"id": "4", "blog": "bmk3037", "status": "todo", "category": "B", "title": "t4", "keyword": "", "landing_url": "", "brief": ""},
        ]
        topics.save(rows, self.csv)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_next_todo_mixes_categories(self):
        picked = topics.next_todo(topics.load(self.csv), 2)
        self.assertEqual([r["id"] for r in picked], ["2", "4"])

    def test_next_todo_fills_when_categories_run_out(self):
        picked = topics.next_todo(topics.load(self.csv), 3)
        self.assertEqual([r["id"] for r in picked], ["2", "4", "3"])

    def test_next_todo_by_blog(self):
        picked = topics.next_todo(topics.load(self.csv), 1, blog="donginensis")
        self.assertEqual([r["id"] for r in picked], ["3"])

    def test_set_status(self):
        topics.set_status("3", "drafted", self.csv)
        self.assertEqual(topics.find(topics.load(self.csv), 3)["status"], "drafted")

    def test_real_topics_file_is_valid(self):
        rows = topics.load()
        self.assertEqual(len({r["id"] for r in rows}), len(rows))
        for r in rows:
            self.assertIn(r["status"], {"todo", "drafted", "published"})
            self.assertTrue(r["landing_url"].startswith("https://donginensis.com/"), r["id"])
            self.assertIn(r["blog"], blogs.ORDER, r["id"])
        keywords = [r["keyword"] for r in rows]
        self.assertEqual(len(set(keywords)), len(keywords), "블로그끼리 같은 핵심 키워드를 쓰면 서로 노출을 깎아 먹습니다")


class GenerateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.topic = {"id": "1", "blog": "donginensis3047", "category": "제품", "title": "t", "keyword": "지능형 제어반",
                      "landing_url": "https://donginensis.com/#product", "brief": "b"}

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def fake_client(self, content, stop_reason="end_turn"):
        message = SimpleNamespace(content=content, stop_reason=stop_reason, stop_details=None)
        stream = mock.MagicMock()
        stream.__enter__.return_value.get_final_message.return_value = message
        client = mock.MagicMock()
        client.beta.messages.stream.return_value = stream
        return client

    def test_call_claude_parses_json_and_skips_refused_part(self):
        content = [
            SimpleNamespace(type="thinking", thinking=""),
            SimpleNamespace(type="text", text='{"partial'),
            SimpleNamespace(type="fallback"),
            SimpleNamespace(type="text", text=json.dumps(SAMPLE_POST, ensure_ascii=False)),
        ]
        client = self.fake_client(content)
        post = generate.call_claude(client, self.topic)
        self.assertEqual(post["title"], SAMPLE_POST["title"])
        kwargs = client.beta.messages.stream.call_args.kwargs
        self.assertEqual(kwargs["model"], "claude-opus-5-5")
        self.assertIn("company_facts", kwargs["system"])

    def test_call_claude_raises_on_refusal(self):
        with self.assertRaises(RuntimeError):
            generate.call_claude(self.fake_client([], "refusal"), self.topic)

    def test_write_post_creates_files(self):
        import datetime as dt
        with mock.patch.object(generate, "POSTS_DIR", self.tmp), mock.patch.object(generate, "ROOT", self.tmp), \
                mock.patch.object(existing, "corpus", return_value=[]):
            out, results = generate.write_post(self.topic, SAMPLE_POST, today=dt.date(2026, 10, 19))
        self.assertEqual(out.name, "2026-10-19-donginensis3047-001")
        self.assertTrue(any(lv == "FAIL" for lv, _ in results))  # 짧은 샘플 글은 분량 미달
        meta = json.loads((out / "meta.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["tags"], ["동인엔시스", "지능형제어반"])
        md = (out / "post.md").read_text(encoding="utf-8")
        self.assertIn("utm_campaign=post001", md)
        self.assertIn("utm_content=donginensis3047", md)
        self.assertEqual(meta["blog"], "donginensis3047")
        issue = (out / "issue.md").read_text(encoding="utf-8")
        self.assertTrue(issue.startswith("<!-- topic-id: 1 -->"))
        self.assertIn("blog.naver.com/donginensis3047", issue)
        self.assertIn("### 자동 검수", issue)
        self.assertIn("사실 확인: 750건 이상 프로젝트", issue)
        preview = (out / "preview.html").read_text(encoding="utf-8")
        self.assertIn("본문 복사", preview)
        self.assertIn("이 글을 올릴 블로그", preview)


class ImageTest(unittest.TestCase):
    def test_image_marker_in_preview_and_issue(self):
        md = "글\n\n[이미지: 02-structure.png]\n\n끝"
        self.assertIn('data-img="02-structure.png"', render.to_html(md))
        self.assertIn('src="images/02-structure.png"', render.to_html(md))
        self.assertIn("이미지 넣기:** `images/02-structure.png`", render.to_issue_markdown(md))

    def test_wrap_adds_logo_and_footer(self):
        from blog import images
        page = images.wrap('<!-- 1200x800 -->\n<div class="frame"><div class="content"><h1>t</h1></div></div>')
        self.assertIn("logo_color.png", page)
        self.assertIn("donginensis.com", page)
        cover = images.wrap(images.cover_fragment("제목 *강조*", "부제", "KICKER", ["태그"]))
        self.assertIn("logo_white.png", cover)
        self.assertIn("<em>강조</em>", cover)


class FromJsonTest(unittest.TestCase):
    def test_from_json_builds_post_and_zip(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            csv_path = tmp / "topics.csv"
            topics.save([{"id": "9", "blog": "donginensis", "status": "todo", "category": "A", "title": "t", "keyword": "k",
                          "landing_url": "https://donginensis.com/", "brief": "b"}], csv_path)
            src = tmp / "post.json"
            src.write_text(json.dumps(SAMPLE_POST, ensure_ascii=False), encoding="utf-8")
            with mock.patch.object(generate, "POSTS_DIR", tmp / "posts"), mock.patch.object(generate, "ROOT", tmp), \
                    mock.patch.object(topics, "TOPICS_CSV", csv_path), \
                    mock.patch.object(topics.load, "__defaults__", (csv_path,)), \
                    mock.patch.object(topics.set_status, "__defaults__", (csv_path,)), \
                    mock.patch.object(existing, "corpus", return_value=[]):
                generate.main(["--id", "9", "--from-json", str(src), "--date", "2026-10-14", "--pack", str(tmp / "out")])
            out = tmp / "posts" / "2026-10-14-donginensis-009"
            self.assertTrue((out / "post.json").exists())
            self.assertTrue((tmp / "out" / "2026-10-14-donginensis-009.zip").exists())
            self.assertEqual(topics.load(csv_path)[0]["status"], "drafted")
        finally:
            shutil.rmtree(tmp)


class PhotoTest(unittest.TestCase):
    PHOTOS = [{"file": "05-photo-a.png", "caption": "배선 작업", "prompt": "Photorealistic control cabinet"}]

    def test_missing_photo_shows_chatgpt_prompt(self):
        out = render.to_html("[사진: 05-photo-a.png]", self.PHOTOS, have=set())
        self.assertIn('data-photo="05-photo-a.png"', out)
        self.assertIn("Photorealistic control cabinet", out)
        self.assertIn("프롬프트 복사", out)
        issue = render.to_issue_markdown("[사진: 05-photo-a.png]", self.PHOTOS, have=set())
        self.assertIn("ChatGPT 프롬프트", issue)

    def test_existing_photo_shows_image(self):
        out = render.to_html("[사진: 05-photo-a.png]", self.PHOTOS, have={"05-photo-a.png"})
        self.assertIn('data-img="05-photo-a.png"', out)
        self.assertNotIn("data-photo", out)

    def test_legacy_photo_slot(self):
        self.assertIn("사진 넣을 자리: 현장 사진", render.to_html("[사진: 현장 사진]"))


class CharCountTest(unittest.TestCase):
    def test_ignores_markers_links_and_markup(self):
        md = "[이미지: 01-cover.png]\n\n## 제목\n\n**굵게** 글 [링크](https://donginensis.com/)"
        self.assertEqual(render.char_count(md), (len("제목\n\n굵게 글 링크"), len("제목굵게글링크")))


class ImageThemeTest(unittest.TestCase):
    def test_field_cover_uses_color_logo_and_blog_label(self):
        from blog import images
        page = images.wrap(images.cover_fragment("t", theme="field"), "동인엔시스 현장 이야기")
        self.assertIn("t-field", page)
        self.assertIn("logo_color.png", page)
        self.assertIn("동인엔시스 현장 이야기", page)
        self.assertEqual(images.blog_of("posts/2026-10-15-donginensis-037"), "donginensis")
        self.assertEqual(images.blog_of("posts/2026-10-15-donginensis3047-001"), "donginensis3047")


def long_post(**kw):
    para = "동인엔시스는 1991년부터 부산에서 제어반을 설계·제작해 온 회사입니다. "
    body = "[이미지: 01-cover.png]\n\n" + para + "펌프 전류 감시 이야기를 합니다.\n\n"
    for i in range(6):
        body += f"## 소제목 {i}\n\n" + "".join(f"펌프 전류 감시 문장 {i}-{j}번은 설비 상태를 알려 줍니다. 값이 쌓이면 흐름이 보입니다 {j}.\n\n"
                                              for j in range(12)) + "\n"
    body += "[이미지: 02-a.png]\n\n[이미지: 03-b.png]\n\n[사진: 05-photo.png]\n\n## 자주 묻는 질문\n\n**Q. 질문?**\n답. 동인엔시스가 돕습니다.\n\n"
    body += "[진단 신청](https://donginensis.com/manufacturing.html#inquiry)"
    post = {"title": "펌프 전류 감시로 읽는 이상 징후, 현장에서 보는 법", "format": "해설형", "body_markdown": body,
            "tags": ["동인엔시스", "지능형제어반", "a", "b", "c", "d", "e", "f"], "personal_prompts": ["q1", "q2"]}
    post.update(kw)
    return post


class QualityTest(unittest.TestCase):
    def levels(self, post, **kw):
        return {lv for lv, _ in quality.check(post, "donginensis3047", "펌프 전류", **kw)}

    def test_flags_overused_keyword_and_banned_words(self):
        res = quality.check(long_post(), "donginensis3047", "펌프 전류")
        self.assertTrue(any("핵심 키워드" in m for lv, m in res if lv == "FAIL"))
        bad = long_post(body_markdown=long_post()["body_markdown"] + "\n\n업계 최고의 제어반")
        self.assertTrue(any("과장 표현" in m for _, m in quality.check(bad, "donginensis3047")))

    def test_two_site_links_and_missing_brand_tag_fail(self):
        p = long_post(tags=["a"] * 8)
        p["body_markdown"] += " [홈](https://donginensis.com/)"
        msgs = [m for lv, m in quality.check(p, "donginensis3047") if lv == "FAIL"]
        self.assertTrue(any("홈페이지 링크 2개" in m for m in msgs))
        self.assertTrue(any("태그에 '지능형제어반' 없음" in m for m in msgs))

    def test_same_format_as_previous_post_fails(self):
        msgs = [m for lv, m in quality.check(long_post(), "donginensis3047", prev_format="해설형") if lv == "FAIL"]
        self.assertTrue(any("형식이 같음" in m for m in msgs))

    def test_five_percent_needs_target_word(self):
        p = long_post()
        p["body_markdown"] += "\n\n전력을 5% 줄였습니다."
        self.assertTrue(any("5%" in m for lv, m in quality.check(p, "donginensis3047") if lv == "FAIL"))


class KeywordTest(unittest.TestCase):
    def test_particles_between_keyword_words(self):
        self.assertEqual(quality._count("OPC UA와 Modbus TCP를 비교합니다", "OPC UA Modbus TCP"), 1)
        self.assertEqual(quality._count("설비 데이터를 수집하고 설비 데이터 수집", "설비 데이터 수집"), 2)
        self.assertEqual(quality._count("설비에서 나온 많은 데이터를 모아서 수집", "설비 데이터 수집"), 0)


class ExistingTest(unittest.TestCase):
    def test_copied_sentence_fails_and_unrelated_passes(self):
        sent = "통신이 끊긴 동안의 측정값은 제어반에 보관했다가 연결이 돌아오면 오래된 순서대로 다시 보냅니다."
        docs = [{"where": "발행됨 x", "title": "다른 글", "text": "앞 문장입니다. " + sent}]
        res = existing.check({"title": "새 글", "body_markdown": "새 내용입니다. " + sent}, docs=docs)
        self.assertTrue(any(lv == "FAIL" and "같은 문장" in m for lv, m in res))
        res = existing.check({"title": "완전히 다른 제목", "body_markdown": "선박 추진 모터 이야기를 길게 씁니다. " * 3}, docs=docs)
        self.assertEqual(res, [])

    def test_contact_line_is_not_counted(self):
        line = "문의 전화 051-862-3668 이메일 dongin@donginmne.com"
        self.assertEqual(existing.sentences(line), [])

    def test_post_text_reads_smart_editor(self):
        page = '<p class="se-text-paragraph se-text-paragraph-align-">안녕하세요 <b>동인엔시스</b>입니다</p>'
        self.assertEqual(existing.post_text(page), "안녕하세요 동인엔시스입니다")


if __name__ == "__main__":
    unittest.main()
