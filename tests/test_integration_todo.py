from lib.todo import Todo
from lib.todo_list import TodoList 

"""
Given I add two todo entries
I see them back in the list
"""

def test_adds_and_shows_incomplete():
    todo_list = TodoList()
    task_1 = Todo("Make a list of todos")
    task_2 = Todo("Watch golden square videos")
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_1, task_2]
    
"""
Given I add two todo entries
Changing one of them to status complete
Returns task that incomplete
"""

def test_adds_two_todo_changing_one_to_complete_status_return_incomplete():
    todo_list = TodoList()
    task_1 = Todo("Make a list of todos")
    task_2 = Todo("Watch golden square videos")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    assert todo_list.incomplete() == [task_2]

"""
Given I add two todo entries
Changing two of them to status complete
Returns an empty list
"""

def test_adds_two_todo_changing_two_to_complete_status_returns_empty_list():
    todo_list = TodoList()
    task_1 = Todo("Make a list of todos")
    task_2 = Todo("Watch golden square videos")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert todo_list.incomplete() == []

"""
Given I add two todo entries
Changing one of them to status complete
Returns task that complete
"""

def test_adds_two_todo_changing_one_to_complete_status_returns_complete():
    todo_list = TodoList()
    task_1 = Todo("Make a list of todos")
    task_2 = Todo("Watch golden square videos")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    assert todo_list.complete() == [task_1]

"""
Given I add two todo entries
Changing two of them to status complete
Returns tasks that complete
"""

def test_adds_two_todo_changing_one_to_complete_status_returns_complete_both():
    todo_list = TodoList()
    task_1 = Todo("Make a list of todos")
    task_2 = Todo("Watch golden square videos")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert todo_list.complete() == [task_1, task_2]

"""
Given I add two todo entries
And I call #give_up
I get all todos as complete by calling #complete
"""

def test_adds_two_todo_calling_give_up_returns_complete_both():
    todo_list = TodoList()
    task_1 = Todo("Make a list of todos")
    task_2 = Todo("Watch golden square videos")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.give_up()
    assert todo_list.complete() == [task_1, task_2]

"""
Given I add two todo entries
And I call #give_up
I get all todos as complete by calling #complete
"""

def test_adds_two_todo_calling_give_up_returns_incomplete_empty_string():
    todo_list = TodoList()
    task_1 = Todo("Make a list of todos")
    task_2 = Todo("Watch golden square videos")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.give_up()
    assert todo_list.incomplete() == []