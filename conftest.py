import pytest
from api.client import APIClient
from config.config import BASE_URL
from api.auth import get_token
from utils.datetime_util import current_time
from playwright.sync_api import sync_playwright

def pytest_configure(config):
    config._metadata = getattr(config, '_metadata', {})
    config._metadata["Execution Date"] = current_time()

@pytest.fixture(scope="session")
def api_client():
    token = get_token(BASE_URL)
    return APIClient(BASE_URL, token)

@pytest.fixture(scope="function")
def playwright_page():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page()
    yield page
    browser.close()
    pw.stop()
