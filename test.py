from typing import Optional, List
class Task:
    def __init__(self, title: str, is_done: bool = False):
        self.title = title
        self.is_done = is_done
    def __repr__(self):
        return f"Task(title: {self.title}, is_done: {self.is_done})"
class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
    def add_task(self, title: str) -> None:
        task = Task(title=title)
        self.tasks.append(task)
    def get_pending(self) -> List[Task]:
        return [task for task in self.tasks if not task.is_done]
    def complete_task(self, title: str) -> None:
        for task in self.tasks:
            if task.title == title:
                task.is_done = True
                print(f"задача '{task}' выполнена")
                return
            print(f"задача '{title}' не найдена")
manager = TaskManager()
manager.add_task("Изучить SQL")
manager.add_task("Поставить Docker")
manager.add_task("Написать API")

print(manager.tasks)        # все задачи
print(manager.get_pending()) # только невыполненные

manager.complete_task("Изучить SQL")

print(manager.get_pending()) # теперь на одну меньше