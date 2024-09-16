from src.method_v1 import Task, delete_task, get_task, post_task, put_task


def main() -> None:
    api_key = "dummy"

    # get
    task = get_task(api_key, 1)

    # post
    new_task = Task(
        title=task.title,
        due_date=task.due_date,
        estimated_days=task.estimated_days,
    )
    post_task(api_key, new_task)

    # put
    updated_task = Task(
        title=task.title,
        due_date=task.due_date,
        estimated_days=task.estimated_days,
    )
    put_task(api_key, 1, updated_task)

    # delete
    delete_task(api_key, 1)


if __name__ == "__main__":
    main()
