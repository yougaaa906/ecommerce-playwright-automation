from pages.base_page import BasePage
import logging
from config.config import KEYWORD


class ProductListPage(BasePage):
    logger = logging.getLogger(__name__)

    # Element locators
    SEARCH_FIELD = "#search-input"
    SORT_SELECT = "#sort-select"
    CATEGORY_MENS_APPAREL = "[data-testid='category-chip-apparel-mens']"
    RESULT_COUNT = "[data-testid='result-count']"
    PRODUCT_NAME = "article[class*='_card_'] div[class*='_name_'] a"

    # Stock status tags
    IN_STOCK_TAG = "[data-testid='stock-badge'][data-stock='in']"
    OUT_OF_STOCK_TAG = "[data-testid='stock-badge'][data-stock='out']"

    # First product card that contains in-stock / out-of-stock tag
    FIRST_IN_STOCK_CARD = f"article:has({IN_STOCK_TAG}) >> nth=0"
    FIRST_OUT_OF_STOCK_CARD = f"article:has({OUT_OF_STOCK_TAG}) >> nth=0"

    def get_result_count_text(self):
        """Get the displayed result count text (e.g., 4 products)"""
        try:
            self.wait_elem_visible(self.RESULT_COUNT)
            self.logger.info("Got result count text")
            return self.get_element_text(self.RESULT_COUNT)
        except Exception as e:
            self.logger.error(f"Failed to get result count: {str(e)}")
            raise

    def get_product_count_number(self):
        """Extract numeric value from result count text"""
        try:
            text = self.get_result_count_text()
            number = int(''.join(filter(str.isdigit, text)))
            self.logger.info(f"Extracted product count: {number}")
            return number
        except Exception as e:
            self.logger.error(f"Failed to extract product number: {str(e)}")
            raise

    def filter_by_mens_apparel(self):
        """Click Men's Apparel category filter"""
        try:
            self.wait_elem_clickable(self.CATEGORY_MENS_APPAREL)
            self.elem_click(self.CATEGORY_MENS_APPAREL)
            self.logger.info("Clicked 'Men's Apparel' successfully")
            self.wait_elem_visible(self.RESULT_COUNT)
            return self.get_result_count_text()
        except Exception as e:
            self.logger.error(f"Failed to click category button: {str(e)}")
            raise

    def sort_products(self, sort_value):
        """Sort products by given sort value"""
        try:
            self.wait_elem_clickable(self.SORT_SELECT)
            self.page.select_option(self.SORT_SELECT, value=sort_value)
            self.logger.info(f"Sorted products by: {sort_value}")
            self.wait_elem_visible(self.RESULT_COUNT)
        except Exception as e:
            self.logger.error(f"Sorting failed: {str(e)}")
            raise

    def get_selected_sort_value(self):
        """Get current selected sort option value"""
        try:
            value = self.page.input_value(self.SORT_SELECT)
            self.logger.info(f"Current sort value: {value}")
            return value
        except Exception as e:
            self.logger.error(f"Failed to get sort value: {str(e)}")
            raise

    def search_product(self, keyword=KEYWORD):
        """Search product by keyword"""
        try:
            self.elem_input(self.SEARCH_FIELD, keyword)
            self.page.press(self.SEARCH_FIELD, "Enter")
            self.wait_elem_visible(self.PRODUCT_NAME)
            self.logger.info(f"Searched product: {keyword}")
        except Exception as e:
            self.logger.error(f"Search failed: {str(e)}")
            raise

    def get_all_product_names(self):
        """Get all product names and return as a list"""
        try:
            self.wait_elem_visible(self.PRODUCT_NAME)
            product_elements = self.page.query_selector_all(self.PRODUCT_NAME)
            names = [element.text_content().strip() for element in product_elements]
            self.logger.info(f"Found {len(names)} products")
            return names
        except Exception as e:
            self.logger.error(f"Failed to get product names: {str(e)}")
            raise

    def click_first_in_stock_product(self):
        """Click on the first product that shows 'In stock' status"""
        try:
            product_locator = self.FIRST_IN_STOCK_CARD
            self.elem_click(product_locator)
            self.logger.info("Clicked first IN STOCK product")
        except Exception as e:
            self.logger.error(f"Failed to click in-stock product: {str(e)}")
            raise

    def click_first_out_of_stock_product(self):
        """Click on the first product that shows 'Out of stock' status"""
        try:
            product_locator = self.FIRST_OUT_OF_STOCK_CARD
            self.elem_click(product_locator)
            self.logger.info("Clicked first OUT OF STOCK product")
        except Exception as e:
            self.logger.error(f"Failed to click out-of-stock product: {str(e)}")
            raise