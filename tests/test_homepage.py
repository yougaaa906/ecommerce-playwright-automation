from pages.home_page import HomePage
import logging

logger = logging.getLogger(__name__)

def test_browsing_homepage_load_and_product_listing(base_page):
    """Test to verify homepage loads and product listing works correctly"""
    logger.info("=== Starting Homepage Browsing Test ===")

    home_page = HomePage(base_page)

    # Verify homepage heading text
    actual_heading = home_page.verify_homepage_loaded()
    assert "Goods made well" in actual_heading, "Hero heading is displayed wrong"

    # Verify product listing is not empty
    product_cards = home_page.get_product_cards()
    assert len(product_cards) > 0, "Product list is empty"

    logger.info("=== Homepage Browsing Test PASSED ===")
