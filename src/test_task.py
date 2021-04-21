from .task import Task


def test():
    task = Task()
    assert task.execute() is True
