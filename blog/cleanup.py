"""오래된 초안의 그림 파일을 저장소에서 지웁니다(저장소 용량 관리).

    python -m blog.cleanup            # 14일이 지난 초안의 images/*.png, photos-src/* 삭제
    python -m blog.cleanup --days 30  # 기준 일수 바꾸기
    python -m blog.cleanup --dry-run  # 지울 목록만 보기

글(post.json·post.md·preview.html·meta.json·issue.md)과 그림 원본(images/*.html)은 남깁니다.
겹침 검사(existing.py)와 형식 검사(generate.prev_format)는 post.json만 쓰므로 영향이 없습니다.
그림은 만들 때 zip으로 전달되고, 지운 파일도 git 기록에는 남아 있어 필요하면 되살릴 수 있습니다.
"""
import argparse
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"


def targets(days):
    cut = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    for d in sorted(POSTS_DIR.iterdir()):
        if d.is_dir() and d.name[:10] < cut:
            yield from sorted((d / "images").glob("*.png"))
            yield from sorted(p for p in (d / "photos-src").glob("*") if p.is_file())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = list(targets(a.days))
    size = sum(f.stat().st_size for f in files)
    for f in files:
        if not a.dry_run:
            f.unlink()
    print(f"{'지울' if a.dry_run else '지운'} 그림 {len(files)}개, {size / 1e6:.1f}MB")


if __name__ == "__main__":
    main()
