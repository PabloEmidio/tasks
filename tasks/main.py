from random import choice
from typing import List

from utils.models.task import (
    Task,
    TaskManager
)
from utils.const import (
    VALID_VALUES,
    SAMPLE_TASKS,
    DEVELOPMENT_EXECUTATION
)


def make_multiple_tasks(how_many_tasks: int) -> List[Task]:
    if DEVELOPMENT_EXECUTATION:
        return [
            Task(task['name'], task['description'])
            for task in SAMPLE_TASKS
        ]
    raise NotImplementedError()


if __name__ == '__main__':
    task_manager = TaskManager()
    for task in make_multiple_tasks(15):
        status = choice(VALID_VALUES)
        task.add_status(status)
        task_manager.add_task(task)
    print(task_manager.get_tasks_by_status('doing'))
