from pages.base_page import BasePage
import logging
from config.config import USERNAME, PASSWORD, FULL_NAME, REG_PWD, CONFIRM_PWD
import random
import string


class AuthPage(BasePage):
    logger = logging.getLogger(__name__)

    ACCOUNT = "[aria-label='Account menu']"
    SIGN_IN_BTN = "[data-testid='account-menu-login']"
    CREATE_ACCOUNT_BTN = "[data-testid='account-menu-register']"

    # Sign in selectors
    EMAIL_FIELD = "[data-testid='login-email']"
    PWD_FIELD = "[data-testid='login-password']"
    LOGIN_SUBMIT_BTN = "[data-testid='login-submit']"
    ERROR_USERNAME_TIP = "[data-testid='login-email-error']"
    ERROR_PWD_TIP = "[data-testid='login-error']"

    # Logout selector
    LOGOUT_BTN = "[data-testid='account-menu-logout']"

    # Create account selectors
    FULL_NAME_FIELD = "[data-testid='register-name']"
    REG_EMAIL_FIELD = "[data-testid='register-email']"
    REG_PWD_FIELD = "[data-testid='register-password']"
    CONFIRM_PWD_FIELD = "[data-testid='register-confirm']"
    REG_SUBMIT_BTN = "[data-testid='register-submit']"
    REG_CONFIRM_ERROR = "[data-testid='register-confirm-error']"

    # Stable click for CI env to avoid intercept/timeout
    def click_account_button_safe(self):
        self.page.wait_for_selector(self.ACCOUNT, state="visible", timeout=15000)
        self.page.click(self.ACCOUNT, force=True)

    # Login with valid credentials
    def login_successed(self, username=USERNAME, password=PASSWORD):
        try:
            self.click_account_button_safe()
            self.elem_click(self.SIGN_IN_BTN)
            self.elem_input(self.EMAIL_FIELD, username)
            self.elem_input(self.PWD_FIELD, password)
            self.elem_click(self.LOGIN_SUBMIT_BTN)
            self.logger.info("User logged in successfully with valid credentials")
            return self.get_element_text(self.ACCOUNT)
        except Exception as e:
            self.logger.error(f"Login failed with valid credentials: {str(e)}")
            raise e

    # Login with invalid username
    def login_invalid_username(self, username="test", password=PASSWORD):
        try:
            self.click_account_button_safe()
            self.elem_click(self.SIGN_IN_BTN)
            self.elem_input(self.EMAIL_FIELD, username)
            self.elem_input(self.PWD_FIELD, password)
            self.elem_click(self.LOGIN_SUBMIT_BTN)
            self.logger.info("Login attempt with invalid username failed as expected")
            return self.get_element_text(self.ERROR_USERNAME_TIP)
        except Exception as e:
            self.logger.error(f"Unexpected successful login with invalid username: {str(e)}")
            raise e

    # Login with invalid password
    def login_invalid_password(self, username=USERNAME, password="123"):
        try:
            self.click_account_button_safe()
            self.elem_click(self.SIGN_IN_BTN)
            self.elem_input(self.EMAIL_FIELD, username)
            self.elem_input(self.PWD_FIELD, password)
            self.elem_click(self.LOGIN_SUBMIT_BTN)
            self.logger.info("Login attempt with invalid password failed as expected")
            return self.get_element_text(self.ERROR_PWD_TIP)
        except Exception as e:
            self.logger.error(f"Unexpected successful login with invalid password: {str(e)}")
            raise e

    # Logout current user
    def logout(self):
        try:
            self.click_account_button_safe()
            self.elem_click(self.LOGOUT_BTN)
            self.logger.info("User logged out successfully")
            return self.get_element_text(self.ACCOUNT)
        except Exception as e:
            self.logger.error(f"Logout failed: {str(e)}")
            raise e

    # Create new account with random email to avoid flakiness
    def create_account(self, fullname=FULL_NAME, reg_pwd=REG_PWD, confirm_pwd=CONFIRM_PWD):
        try:
            random_str = ''.join(random.choices(string.ascii_lowercase, k=8))
            reg_email = f"test_{random_str}@icloud.com"

            self.click_account_button_safe()
            self.elem_click(self.CREATE_ACCOUNT_BTN)
            self.elem_input(self.FULL_NAME_FIELD, fullname)
            self.elem_input(self.REG_EMAIL_FIELD, reg_email)
            self.elem_input(self.REG_PWD_FIELD, reg_pwd)
            self.elem_input(self.CONFIRM_PWD_FIELD, confirm_pwd)
            self.elem_click(self.REG_SUBMIT_BTN)
            self.wait_elem_visible(self.ACCOUNT)

            self.logger.info(f"New account created with random email: {reg_email}")
            return self.get_element_text(self.ACCOUNT)
        except Exception as e:
            self.logger.error(f"Failed to create new account: {str(e)}")
            raise e

    # Create account with mismatched password confirmation
    def create_account_error_confirm_pwd(self, fullname=FULL_NAME, reg_pwd=REG_PWD, confirm_pwd="123"):
        try:
            random_str = ''.join(random.choices(string.ascii_lowercase, k=8))
            reg_email = f"test_{random_str}@icloud.com"

            self.click_account_button_safe()
            self.elem_click(self.CREATE_ACCOUNT_BTN)
            self.elem_input(self.FULL_NAME_FIELD, fullname)
            self.elem_input(self.REG_EMAIL_FIELD, reg_email)
            self.elem_input(self.REG_PWD_FIELD, reg_pwd)
            self.elem_input(self.CONFIRM_PWD_FIELD, confirm_pwd)
            self.elem_click(self.REG_SUBMIT_BTN)
            self.wait_elem_visible(self.REG_CONFIRM_ERROR)

            self.logger.info(f"Register check with random email: {reg_email}")
            return self.get_element_text(self.REG_CONFIRM_ERROR)
        except Exception as e:
            self.logger.error(f"Unexpected successful account creation with mismatched password: {str(e)}")
            raise e
