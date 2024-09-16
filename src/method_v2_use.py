from src.method_v2 import Task, TaskAPIClient


def main() -> None:
    client = TaskAPIClient(api_key="dummy")

    # get
    task = client.get_task(1)

    # post
    new_task = Task(
        title=task.title,
        due_date=task.due_date,
        estimated_days=task.estimated_days,
    )
    client.post_task(new_task)

    # put
    updated_task = Task(
        title=task.title,
        due_date=task.due_date,
        estimated_days=task.estimated_days,
    )
    client.put_task(1, updated_task)

    # delete
    client.delete_task(1)


if __name__ == "__main__":
    main()
