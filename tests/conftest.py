import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage
from config.config import TEST_URL


@pytest.fixture(scope="function")
def navigate_to_product_list(page: Page):
    """Navigate to product list page from home"""
    page.goto(TEST_URL)
    home_page = HomePage(page)
    home_page.click_shop_all()
    yield page


@pytest.fixture(scope="function")
def navigate_to_in_stock_product(page: Page, navigate_to_product_list):
    """Navigate to first in-stock product"""
    product_list = ProductListPage(page)
    product_list.filter_by_mens_apparel()
    product_list.click_first_in_stock_product()
    yield


@pytest.fixture(scope="function")
def navigate_to_out_of_stock_product(page: Page, navigate_to_product_list):
    """Navigate to first out-of-stock product"""
    product_list = ProductListPage(page)
    product_list.filter_by_mens_apparel()
    product_list.click_first_out_of_stock_product()
    yield


@pytest.fixture(scope="function")
def navigate_to_checkout_page(page: Page, navigate_to_in_stock_product):
    """Navigate to checkout page with item in cart"""
    product_detail = ProductDetailPage(page)
    product_detail.add_to_cart()
    product_detail.cart_operation()
    product_detail.go_to_checkout()
    yield
