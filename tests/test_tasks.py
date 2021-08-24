from unittest.mock import Mock

import pytest

from tasks.utils.models.task import Task
from tasks.utils.exceptions import StatusError


@pytest.fixture
def task() -> Task:
    return Task(Mock(), Mock())


@pytest.mark.parametrize(
    'is_valid_status, status',
    (
        (True, 'done'),
        (True, 'Done'),
        (True, 'DONE'),
        (True, 'failed'),
        (False, 'seeing'),
    )
)
def test_task_add_status(is_valid_status: bool, status: str, task: Task) -> None:
    if not is_valid_status:
        with pytest.raises(StatusError):
            task.add_status(status)
    else:
        task.add_status(status)
        assert task.status == status.lower()
