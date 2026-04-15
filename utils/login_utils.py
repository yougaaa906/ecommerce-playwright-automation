from pages.auth_page import AuthPage


def login(page):
    auth_page = AuthPage(page)
    auth_page.login_successed()