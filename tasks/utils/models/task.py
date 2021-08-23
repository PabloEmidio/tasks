from ..descriptors import StatusDescriptor

# tasks = [
#     {
#         'task_id': 1,
#         'task_name': 'test 01',
#         'description': 'Description test 01',
#         'status': 'done'

#     },
#     {
#         'task_id': 2,
#         'task_name': 'test 02',
#         'description': 'Description test 02',
#         'status': 'doing'

#     },
# ]


class Task:
    status: str = StatusDescriptor()

    def __init__(self, name: str, description: str) -> None:
        self._name = name
        self._description = description
        self.status = 'todo'

    def add_status(self, status: str):
        self.status = status
