from lib.todo import Todo

"""
Initializing todo
"""

def test_initialize_todo():
    task_1 = Todo("Make a list of todos")
    assert task_1.task == "Make a list of todos"
    assert task_1.complete == False

"""
After initialising,
    #mark_complete status to True
"""

def test_initialize_todo_and_mark_complete():
    task_1 = Todo("Make a list of todos")
    task_1.mark_complete() 
    assert task_1.complete ==  True