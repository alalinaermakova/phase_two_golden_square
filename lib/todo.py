class Todo:

    def __init__(self, task):
        self.task = task
        self.complete = False

    def mark_complete(self):
        if self.complete == False:
            self.complete = True