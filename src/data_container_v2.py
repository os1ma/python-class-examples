from datetime import datetime, timedelta, timezone
from typing import Any

JST = timezone(timedelta(hours=9))


def calculate_start_deadline(task: dict[str, Any]) -> datetime:
    due_date = task["due_date"]
    estimated_days = task["estimated_days"]
    return due_date - timedelta(days=estimated_days)


def main() -> None:
    task = {
        "title": "スライドの作成",
        "due_date": datetime(2024, 9, 19, tzinfo=JST),
        "estimated_days": 7,
    }
    start_deadline = calculate_start_deadline(task)

    print(f"着手デッドライン: {start_deadline.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    main()
