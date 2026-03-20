import os

ENV = os.getenv("ENV", "dev")

BASE_URLS = {
    "dev": "https://reqres.in/api",
    "stage": "https://reqres.in/api",
    "prod": "https://reqres.in/api"
}

BASE_URL = BASE_URLS.get(ENV)
