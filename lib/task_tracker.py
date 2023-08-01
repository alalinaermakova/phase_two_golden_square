class TaskTracker:
        def __init__(self):
            self.my_list = []

        def add(self, task):
            return self.my_list.append(task)

        def list_tasks(self):
            if len(self.my_list) == 0:
                print(self.my_list)
                raise Exception("No tasks were given")
            else:
                return self.my_list

        def remove_task(self, task):
            return self.my_list.remove(task)