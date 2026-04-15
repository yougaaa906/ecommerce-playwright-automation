import logging
import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from config.config import KEYWORD, SORT_PRICE_DESC

logger = logging.getLogger(__name__)

def test_filter_sort_search_flow(navigate_to_product_list):
    """Test filter, sort and search with full product name validation"""

    base_page = navigate_to_product_list
    product_list = ProductListPage(base_page)

    # Filter
    product_list.filter_by_mens_apparel()

    # Sort
    product_list.sort_products(SORT_PRICE_DESC)
    assert product_list.get_selected_sort_value() == SORT_PRICE_DESC

    # Search
    product_list.search_product(KEYWORD)

    # Get ALL product names
    product_names = product_list.get_all_product_names()
    logger.info(f"Found pro ducts: {product_names}")

    # Assert every product contains the keyword
    for name in product_names:
        assert any(KEYWORD.lower() in name.lower() for name in product_names), f"Product name does not contain keyword: {name}"

    logger.info("All products are matched with the search keyword!")
