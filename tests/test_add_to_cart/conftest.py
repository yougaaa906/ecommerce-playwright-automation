import pytest
from pages.product_detail_page import ProductDetailPage

@pytest.fixture(scope="function", autouse=True)
def clear_cart_after_test(base_page):
    """Clear cart after each cart-related test to prevent data pollution"""
    yield
    product_page = ProductDetailPage(base_page)
    product_page.clear_cart()
