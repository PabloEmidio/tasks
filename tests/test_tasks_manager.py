import pytest

from tasks.utils.models.task import (
    Task,
    TaskManager
)
from .conftest import make_multiple_tasks

@pytest.fixture
def task_manager():
    task_manager = TaskManager()
    for task in make_multiple_tasks():
        task_manager.add_task(task)
    return task_manager

@pytest.mark.parametrize(
    'is_valid_task, task',
    (
        (True, Task('test', 'test')),
        (False, 'Task()')
    )
)
def test_generic(is_valid_task, task, task_manager):
    if not is_valid_task:
        with pytest.raises(TypeError):
            task_manager.add_task(2)
    else:
        task.add_status('failed')
        task_manager.add_task(task)
        assert task_manager.get_tasks_by_status('failed')
