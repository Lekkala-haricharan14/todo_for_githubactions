class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task or task.strip() == "":
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)
        return task

    def delete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        return self.tasks.pop(index)

    def get_tasks(self):
        return self.tasks
