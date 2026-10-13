"""주제 상태 바꾸기: python -m blog.mark --id 17 --status published"""
import argparse

from blog import topics

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    parser.add_argument("--status", default="published", choices=["todo", "drafted", "published"])
    args = parser.parse_args()
    topics.set_status(args.id, args.status)
    print(f"주제 {args.id} → {args.status}")
