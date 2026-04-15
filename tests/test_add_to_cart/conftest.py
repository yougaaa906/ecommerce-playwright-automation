import pytest
from pages.product_detail_page import ProductDetailPage

@pytest.fixture(scope="function", autouse=True)
def clear_cart_after_test(page):
    """Clear cart after each cart-related test to prevent data pollution"""
    yield
    product_page = ProductDetailPage(page)
    product_page.clear_cart()