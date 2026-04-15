import pytest
import os
import logging
from datetime import datetime
from playwright.sync_api import Page
from utils.login_utils import login
from pages.home_page import HomePage

def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)

    return root_logger

logger = setup_logging()

@pytest.fixture(scope="function")
def base_page(page: Page):
    page.goto("http://localhost:5173")
    yield page

@pytest.fixture
def logged_in_page(base_page: Page):
    login(base_page)
    yield base_page

@pytest.fixture(scope="function")
def handle_cookie_consent(base_page, request):
    if "cookie_test" in request.keywords:
        yield
        return

    try:
        home_page = HomePage(base_page)
        if home_page.is_cookie_banner_visible():
            home_page.click_accept_all_cookies()
            logger.info("Auto-accepted cookie consent banner")
    except Exception:
        logger.info("No cookie banner detected")
    yield

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call":
        if rep.failed:
            logger.error(f"FAILED: {item.name}")
            try:
                page = item.funcargs.get("base_page") or item.funcargs.get("logged_in_page")
                os.makedirs("screenshots", exist_ok=True)
                page.screenshot(path=f"screenshots/fail_{item.name}.png", full_page=True)
            except:
                pass
        else:
            logger.info(f"PASSED: {item.name}")
