from locust import HttpUser, TaskSet, task, between
from random import randint


class CommentUserBehavior(TaskSet):
    def on_start(self):
        r = self.client.get("/")

    @task
    def posts(self):
        self.client.get("/post")

    @task
    def comment(self):
        data = {
            "id": randint(1, 100),
            "name": f"my comment #{randint(1,200)}",
            "email": "test@user.habr",
            "body": "Author is cool. Some text. Hello world!"
        }
        self.client.post("/comments", data)


class TodoUserBehavior(TaskSet):
    @task
    def todos(self):
        self.client.get("/todos")

    @task
    def add_todo(self):
        data = {
            "id": randint(1, 100),
            "title": "make Highload homework",
            "completed": False
        }
        self.client.post("/todos", data)


class dbUserBehavior(TaskSet):
    @task
    def db(self):
        self.client.get("/db")


class WebsiteUser(HttpUser):
    tasks = [CommentUserBehavior, TodoUserBehavior, dbUserBehavior]
    wait_time = between(1, 2)
