# main.py
import requests
from user_todos import UserTodos

def get_all_todos(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        user_todos = UserTodos(data)
        return user_todos
    else:
        return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/todos"
    user_todos = get_all_todos(api_url)

    if user_todos:
        for t in user_todos:
            print(f"User ID: {t.userId}, Todo ID: {t.id}, Title: {t.title}, Completed: {t.completed}")
    else:
        print("Failed to fetch todos.")
