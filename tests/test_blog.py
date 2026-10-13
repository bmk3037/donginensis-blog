import json
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from blog import generate, render, topics

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
            {"id": "1", "status": "published", "category": "A", "title": "t1", "keyword": "", "landing_url": "", "brief": ""},
            {"id": "2", "status": "todo", "category": "A", "title": "t2", "keyword": "", "landing_url": "", "brief": ""},
            {"id": "3", "status": "todo", "category": "A", "title": "t3", "keyword": "", "landing_url": "", "brief": ""},
            {"id": "4", "status": "todo", "category": "B", "title": "t4", "keyword": "", "landing_url": "", "brief": ""},
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

    def test_set_status(self):
        topics.set_status("3", "drafted", self.csv)
        self.assertEqual(topics.find(topics.load(self.csv), 3)["status"], "drafted")

    def test_real_topics_file_is_valid(self):
        rows = topics.load()
        self.assertEqual(len({r["id"] for r in rows}), len(rows))
        for r in rows:
            self.assertIn(r["status"], {"todo", "drafted", "published"})
            self.assertTrue(r["landing_url"].startswith("https://donginensis.com/"), r["id"])


class GenerateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.topic = {"id": "1", "category": "제품", "title": "t", "keyword": "지능형 제어반",
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
        with mock.patch.object(generate, "POSTS_DIR", self.tmp), mock.patch.object(generate, "ROOT", self.tmp):
            out = generate.write_post(self.topic, SAMPLE_POST, today=dt.date(2026, 10, 19))
        self.assertEqual(out.name, "2026-10-19-001")
        meta = json.loads((out / "meta.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["tags"], ["동인엔시스", "지능형제어반"])
        self.assertIn("utm_campaign=post001", (out / "post.md").read_text(encoding="utf-8"))
        issue = (out / "issue.md").read_text(encoding="utf-8")
        self.assertTrue(issue.startswith("<!-- topic-id: 1 -->"))
        self.assertIn("사실 확인: 750건 이상 프로젝트", issue)
        self.assertIn("본문 복사", (out / "preview.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()


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
            topics.save([{"id": "9", "status": "todo", "category": "A", "title": "t", "keyword": "k",
                          "landing_url": "https://donginensis.com/", "brief": "b"}], csv_path)
            src = tmp / "post.json"
            src.write_text(json.dumps(SAMPLE_POST, ensure_ascii=False), encoding="utf-8")
            with mock.patch.object(generate, "POSTS_DIR", tmp / "posts"), mock.patch.object(generate, "ROOT", tmp), \
                    mock.patch.object(topics, "TOPICS_CSV", csv_path), \
                    mock.patch.object(topics.load, "__defaults__", (csv_path,)), \
                    mock.patch.object(topics.set_status, "__defaults__", (csv_path,)):
                generate.main(["--id", "9", "--from-json", str(src), "--date", "2026-10-14", "--pack", str(tmp / "out")])
            out = tmp / "posts" / "2026-10-14-009"
            self.assertTrue((out / "post.json").exists())
            self.assertTrue((tmp / "out" / "2026-10-14-009.zip").exists())
            self.assertEqual(topics.load(csv_path)[0]["status"], "drafted")
        finally:
            shutil.rmtree(tmp)
