import pytest
from todo import ToDoList

def test_add_task():
    todo = ToDoList()
    todo.add_task("Task 1")
    assert todo.get_tasks() == ["Task 1"]

def test_add_empty_task():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.add_task("")

def test_delete_task():
    todo = ToDoList()
    todo.add_task("Task 1")
    removed = todo.delete_task(0)
    assert removed == "Task 1"
    assert todo.get_tasks() == []

def test_delete_invalid_index():
    todo = ToDoList()
    todo.add_task("Task 1")
    with pytest.raises(IndexError):
        todo.delete_task(5)
