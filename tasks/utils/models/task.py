from typing import List

from ..const import VALID_VALUES
from ..descriptors import StatusDescriptor
from ..exceptions import StatusError


class Task:
    status: str = StatusDescriptor()

    def __init__(self, name: str, description: str) -> None:
        self._name = name
        self._description = description
        self.status = 'todo'

    def add_status(self, status: str) -> None:
        self.status = status

    def __str__(self) -> str:
        return f'Task({self._name}, status={self.status})'

    def __repr__(self) -> str:
        return str(self)


class TaskManager:
    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            msg = f'task must be \'{Task}\', given \'{type(task)}\''
            raise TypeError(msg)
        self._tasks.append(task)

    def __len__(self):
        return len(self._tasks)

    def __getitem__(self, item) -> Task:
        return self._tasks[item]

    def get_tasks_by_status(self, status: str) -> List[Task]:
        if status not in VALID_VALUES:
            raise StatusError('', status)
        return [
            task
            for task in self._tasks
            if task.status == status
        ]
