from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=9))


class Task:
    def __init__(self, title: str, due_date: datetime, estimated_days: int):
        self.title = title
        self.due_date = due_date
        self.estimated_days = estimated_days


def calculate_start_deadline(task: Task) -> datetime:
    return task.due_date - timedelta(days=task.estimated_days)


def main() -> None:
    task = Task("スライドの作成", datetime(2024, 9, 19, tzinfo=JST), estimated_days=7)
    start_deadline = calculate_start_deadline(task)

    print(f"着手デッドライン: {start_deadline.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    main()
