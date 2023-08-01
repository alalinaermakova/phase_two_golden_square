1. Describe the problem

    -User needs to keep track of their tasks,
    they can add todo tasks to and see a list of them.

    -User needs to focus on tasks to complete,
    mark tasks as complete and have them disappear from the list.

2. Design the Class Interface

    class TaskTracker:
        def __init__(self):
            pass

        def add(self, task):
            # Parameters:
            #    task: string represents a single task
            # Returns:
            #    nothing
            # What does:
            #    Saves tasks to the self object
            pass

        def list_tasks(self):
            # Returns:
            #    a list of task that was added
            #    list =["Walk the dog"]
            # Side-effects:
            #    Throws an exception if no task is set
            #    raise Exception("No tasks were given")
            pass

        def remove_task(self, task):
            # Parameters:
            #    task: string represents a single task
            #    status: string represents completed status
            # What does:
            #    Removes the task from the list
            pass


3. Create Examples as Tests
    """
    Initially there is no tasks to display
    """

    tasker = TaskTracker()
    tasker.list_tasks() ==> []

    """
    Given a task
    # add task to the list
    # display one task in the list
    """

    tasker = TaskTracker()
    tasker.add("Walk the dog")
    tasker.list_tasks() ==> ["Walk the dog"]

    """
    Given a task
    # add 2 task to the list
    # display 2 task in the list
    """

    tasker = TaskTracker()
    tasker.add("Walk the dog")
    tasker.add("Wash the dishes")
    tasker.list_tasks() ==> ["Walk the dog","Wash the dishes"]

    """
    Given task with status as copmleted
    Returns a list without this task
    """

    tasker = TaskTracker()
    tasker.add("Walk the dog")
    tasker.remove_task("Wash the dishes")
    tasker.list_tasks() ==> ["Walk the dog"]

    """
    Throwing an exception when task weren't given
    """

    tasker = TaskTracker()
    tasker.list_tasks() ==> "No tasks were given"

