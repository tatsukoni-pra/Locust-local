from locust import HttpUser, task, constant_pacing

class HelloWorldUser(HttpUser):
    #  1タスク = 1秒間に1回リクエストを送信する
    wait_time = constant_pacing(1)

    @task
    def hello_world(self):
        self.client.get("/hello-world")
