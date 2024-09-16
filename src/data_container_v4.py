from datetime import date, timedelta


class Task:
    def __init__(self, title: str, due_date: date, estimated_days: int) -> None:
        self.title = title
        self.due_date = due_date
        self.estimated_days = estimated_days

    def start_deadline(self) -> date:
        return self.due_date - timedelta(days=self.estimated_days)


def main() -> None:
    task = Task("スライドの作成", date(2024, 9, 19), estimated_days=7)
    start_deadline = task.start_deadline()

    print(f"着手デッドライン: {start_deadline.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    main()
