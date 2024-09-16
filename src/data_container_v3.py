from datetime import date, timedelta


class Task:
    def __init__(self, title: str, due_date: date, estimated_days: int):
        self.title = title
        self.due_date = due_date
        self.estimated_days = estimated_days


def calculate_start_deadline(task: Task) -> date:
    return task.due_date - timedelta(days=task.estimated_days)


def main() -> None:
    task = Task("スライドの作成", date(2024, 9, 19), estimated_days=7)
    start_deadline = calculate_start_deadline(task)

    print(f"着手デッドライン: {start_deadline.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    main()
