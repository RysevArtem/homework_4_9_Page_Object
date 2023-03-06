import pytest
from selene.support.shared import browser
import os


@pytest.fixture(scope='function')
def browser_options():
    browser.config.window_height = os.getenv('height', 1024)
    browser.config.window_width = os.getenv('width', 768)
    browser.config.base_url = os.getenv('base_url', 'https://demoqa.com')

    yield
