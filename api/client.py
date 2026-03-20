import requests
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = token

        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500,502,503,504])
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def request(self, method, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        response = self.session.request(method, url, json=payload, headers=headers)
        return response
