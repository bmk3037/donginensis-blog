"""topics.csv 읽기/쓰기. status: todo → drafted → published"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS_CSV = ROOT / "topics.csv"
FIELDS = ["id", "status", "category", "title", "keyword", "landing_url", "brief"]


def load(path=TOPICS_CSV):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def save(rows, path=TOPICS_CSV):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def find(rows, topic_id):
    for row in rows:
        if row["id"] == str(topic_id):
            return row
    raise KeyError(f"topics.csv에 id={topic_id} 주제가 없습니다")


def next_todo(rows, count=1):
    """아직 쓰지 않은 주제를 위에서부터 count개. 같은 분류가 연달아 나오지 않게 고릅니다."""
    picked, used_categories = [], set()
    todo = [r for r in rows if r["status"] == "todo"]
    for row in todo:
        if len(picked) == count:
            break
        if row["category"] not in used_categories:
            picked.append(row)
            used_categories.add(row["category"])
    for row in todo:  # 분류가 모자라면 남은 것으로 채움
        if len(picked) == count:
            break
        if row not in picked:
            picked.append(row)
    return picked


def set_status(topic_id, status, path=TOPICS_CSV):
    rows = load(path)
    find(rows, topic_id)["status"] = status
    save(rows, path)
