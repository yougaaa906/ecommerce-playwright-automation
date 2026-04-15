import logging
import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage


logger = logging.getLogger(__name__)

def is_add_to_cart_disabled(self):
    """Check if Add to Cart button is disabled"""
    try:
        self.wait_elem_visible(self.ADD_TO_CART_BTN)
        is_disabled = self.page.locator(self.ADD_TO_CART_BTN).is_disabled()
        self.logger.info(f"Add to Cart button disabled status: {is_disabled}")
        return is_disabled
    except Exception as e:
        self.logger.error(f"Error checking button status: {str(e)}")
        raise