from lib.task_tracker import *
import pytest

"""
Given a task
# add task to the list
# display one task in the list
"""

def test_task_tracker_add_task():
    tasker = TaskTracker()
    tasker.add("Walk the dog")
    result = tasker.list_tasks()
    assert result == ["Walk the dog"]

"""
Given a task
# add 2 task to the list
# display 2 task in the list
"""

def test_task_tracker_add_two_tasks():
    tasker = TaskTracker()
    tasker.add("Walk the dog")
    tasker.add("Wash the dishes")
    result = tasker.list_tasks()
    assert result == ["Walk the dog","Wash the dishes"]

"""
Given task with status as copmleted
Returns a list without this task
"""

def test_remove_task():
    tasker = TaskTracker()
    tasker.add("Walk the dog")
    tasker.add("Wash the dishes")
    tasker.remove_task("Wash the dishes")
    result = tasker.list_tasks()
    assert result == ["Walk the dog"]

"""
Throwing an exception when task weren't given
"""

def test_list_no_tasks():
    with pytest.raises(Exception) as error:
        tasker = TaskTracker()
        tasker.list_tasks()
    assert str(error.value) == "No tasks were given"