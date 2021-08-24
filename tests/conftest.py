from typing import List

from tasks.utils.const import SAMPLE_TASKS
from tasks.utils.models.task import Task

def make_multiple_tasks() -> List[Task]:
    return [
        Task(task['name'], task['description'])
        for task in SAMPLE_TASKS
    ]
