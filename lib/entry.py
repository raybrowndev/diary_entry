class Entry:
    def __init__(self, date, description):
        self.date = date
        self.description = description
        self.task = []
        self.contact = {}
    
    def add_task(self, task):
        self.task.append(task)  # Add a task to the list of tasks

    def add_contact(self, name, number):
        self.contact[name] = number 
