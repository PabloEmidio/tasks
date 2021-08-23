from utils.models.task import Task


if __name__ == '__main__':
    task = Task('study', 'Study tdd and mock status')
    task.add_status('done')
    task.add_status('doing')
    print(task.status)
