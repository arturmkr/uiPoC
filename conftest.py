import pytest
from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright
from selene import Browser, Config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser_selene():
    browser = Browser(
        Config(
            driver=webdriver.Chrome(ChromeDriverManager().install()),
            base_url="https://arturmkr.github.io/simple_web_site",
            timeout=4,
            window_width=1920,
            window_height=1080
        )
    )
    yield browser
    browser.close_current_tab()


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser_playwright(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
