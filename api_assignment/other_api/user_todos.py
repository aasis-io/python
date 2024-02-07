# user_todos.py
class Todos:
    def __init__(self, data: dict):
        self.userId = data['userId']
        self.id = data['id']
        self.title = data['title']
        self.completed = data['completed']

class UserTodos:
    def __init__(self, todos_data):
        self.todos_list = [Todos(todo) for todo in todos_data]

    def __iter__(self):
        return iter(self.todos_list)
