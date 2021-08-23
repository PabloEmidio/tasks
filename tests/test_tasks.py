import unittest
from unittest.mock import Mock

from tasks.utils.models.task import Task
from tasks.utils.exceptions import StatusError

class TestPoha(unittest.TestCase):
    def setUp(self) -> None:
        self.task = Task(Mock(), Mock())
    
    def test_error(self):
        with self.assertRaises(StatusError):
            self.task.add_status('seeing')
