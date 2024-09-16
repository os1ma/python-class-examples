from datetime import datetime


class Task:
    def __init__(self, title: str, due_date: datetime, estimated_days: int):
        self.title = title
        self.due_date = due_date
        self.estimated_days = estimated_days


def get_task(api_key: str, task_id: int) -> Task:
    # 実際にはAPIを呼び出してデータを取得する
    raise NotImplementedError


def post_task(api_key: str, task: Task) -> None:
    raise NotImplementedError


def put_task(api_key: str, task_id: int, task: Task) -> None:
    raise NotImplementedError


def delete_task(api_key: str, task_id: int) -> None:
    raise NotImplementedError
