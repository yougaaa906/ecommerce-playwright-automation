import logging
from pages.home_page import HomePage
import pytest

logger = logging.getLogger(__name__)

@pytest.mark.cookie_test
def test_homepage_cookie_banner_appears(page):
    """Test to verify cookie consent banner is displayed on initial load"""
    logger.info("=== Starting Cookie Banner Display Test ===")
    home_page = HomePage(page)

    # Assert banner is visible
    assert home_page.is_cookie_banner_visible(), "Cookie banner is not displayed"
    logger.info("Cookie banner is visible")
    logger.info("=== Cookie Banner Test PASSED ===")

@pytest.mark.cookie_test
def test_homepage_accept_all_cookies(page):
    """Test to accept all cookies via the banner"""
    logger.info("=== Starting Accept All Cookies Test ===")
    home_page = HomePage(page)

    # Verify banner is present first
    assert home_page.is_cookie_banner_visible(), "Cookie banner is not displayed"

    # Perform action
    home_page.click_accept_all_cookies()

    logger.info("=== Accept All Cookies Test PASSED ===")

@pytest.mark.cookie_test
def test_homepage_decline_cookies(page):
    """Test to decline cookies via the banner"""
    logger.info("=== Starting Decline Cookies Test ===")
    home_page = HomePage(page)

    home_page.is_cookie_banner_visible()
    home_page.click_decline_cookies()
    logger.info("=== Decline Cookies Test PASSED ===")