# mypy: disable-error-code="no-untyped-def"


from datetime import date, timedelta


def calculate_start_deadline(task):
    due_date = task["due_date"]
    estimated_days = task["estimated_days"]
    return due_date - timedelta(days=estimated_days)


def main() -> None:
    task = {
        "title": "スライドの作成",
        "due_date": date(2024, 9, 19),
        "estimated_days": 7,
    }
    start_deadline = calculate_start_deadline(task)

    print(f"着手デッドライン: {start_deadline.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    main()
