from locust import HttpUser, task, between
from threading import Lock
import os

MAX_REQUESTS = 10


class ReqResUser(HttpUser):

    host = "https://reqres.in"
    wait_time = between(2, 4)

    # Shared request counter across all simulated users
    requests_started = 0
    request_lock = Lock()

    def on_start(self):
        api_key = os.getenv("REQRES_API_KEY")

        if not api_key:
            raise RuntimeError(
                "REQRES_API_KEY is not configured in the terminal."
            )

        self.client.headers.update({
            "x-api-key": api_key
        })

    @task
    def get_users(self):

        # Reserve a request slot before sending the request
        with ReqResUser.request_lock:

            if ReqResUser.requests_started >= MAX_REQUESTS:
                self.environment.runner.quit()
                return

            ReqResUser.requests_started += 1

        with self.client.get(
            "/api/users?page=2",
            name="GET /api/users?page=2",
            catch_response=True
        ) as response:

            print("Status Code:", response.status_code)

            if response.status_code == 200:
                response.success()

            elif response.status_code == 429:
                response.failure("Rate limited: HTTP 429")

                # Stop immediately if the API rate-limits us
                self.environment.runner.quit()

            else:
                response.failure(
                    f"Unexpected status code: {response.status_code}"
                )

        # Stop when the request limit is reached
        if ReqResUser.requests_started >= MAX_REQUESTS:
            self.environment.runner.quit()