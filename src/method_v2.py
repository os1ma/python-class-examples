from datetime import datetime


class Task:
    def __init__(self, title: str, due_date: datetime, estimated_days: int):
        self.title = title
        self.due_date = due_date
        self.estimated_days = estimated_days


class TaskAPIClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_task(self, task_id: int) -> Task:
        # 実際にはAPIを呼び出してデータを取得する
        raise NotImplementedError

    def post_task(self, task: Task) -> None:
        raise NotImplementedError

    def put_task(self, task_id: int, task: Task) -> None:
        raise NotImplementedError

    def delete_task(self, task_id: int) -> None:
        raise NotImplementedError
