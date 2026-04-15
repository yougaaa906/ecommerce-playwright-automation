from pages.auth_page import AuthPage
import logging

logger = logging.getLogger(__name__)


def test_login_successfully(base_page):
    """Test case for successful user login with valid credentials"""
    logger.info("=== Starting test_login_successfully ===")

    auth = AuthPage(base_page)
    account_text = auth.login_successed()

    assert "Test" in account_text, "Login failed: Account name does not match"
    logger.info("Test test_login_successfully passed successfully")


def test_login_error_pwd(base_page):
    """Test case for user login with invalid password"""
    logger.info("=== Starting test_login_error_pwd ===")

    auth = AuthPage(base_page)
    error_tip_text = auth.login_invalid_password()

    assert "Invalid email or password" in error_tip_text, "Login failed: Invalid password"
    logger.info("Test test_login_error_pwd passed successfully")


def test_login_error_username(base_page):
    """Test case for user login with invalid username"""
    logger.info("=== Starting test_login_error_username ===")

    auth = AuthPage(base_page)
    error_tip_text = auth.login_invalid_username()

    assert "Enter a valid email address" in error_tip_text, "Login failed: Invalid email address"
    logger.info("Test test_login_error_username passed successfully")


def test_logout(logged_in_page):
    """Test case for user logout functionality"""
    logger.info("=== Starting test_logout ===")

    auth = AuthPage(logged_in_page)
    logout_result_text = auth.logout()

    assert "Account" in logout_result_text, "Log out failed"
    logger.info("Test test_logout passed successfully")


def test_register_error_confirm_pwd(base_page):
    """Test case for user register with password mismatch"""
    logger.info("=== Starting test_register_error_confirm_pwd ===")

    auth = AuthPage(base_page)
    error_tip_text = auth.create_account_error_confirm_pwd()

    assert "Passwords do not match" in error_tip_text, "Create account failed"
    logger.info("Test test_register_error_confirm_pwd passed successfully")


def test_register_successfully(base_page):
    """Test case for successful user register"""
    logger.info("=== Starting test_register_successfully ===")

    auth = AuthPage(base_page)
    account_name = auth.create_account()

    assert "test001" in account_name, "Create account failed"
    logger.info("Test test_register_successfully passed successfully")
