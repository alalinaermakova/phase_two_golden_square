class TodoList:
    def __init__(self):
        self.my_list = []

    def add(self, todo):
        self.my_list.append(todo)

    def incomplete(self):
        incomplete_list= []
        for item in self.my_list:
            if item.complete == False:
                incomplete_list.append(item)
        return incomplete_list

    def complete(self):
        complete_list= []
        for item in self.my_list:
            if item.complete == True:
                complete_list.append(item)
        return complete_list

    def give_up(self):
        give_up_list = []
        for item in self.my_list:
            if item.complete == False:
                item.complete = True
                give_up_list.append(item)
        return give_up_list