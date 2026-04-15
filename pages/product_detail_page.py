from pages.base_page import BasePage
import logging


class ProductDetailPage(BasePage):
    logger = logging.getLogger(__name__)

    # Element locators
    SIZE_BTN = "[data-testid='size-option-S']"
    ADD_NUM_BTN = "[data-testid='qty-increment']"
    ADD_TO_CART_BTN = "[data-testid='add-to-cart']"
    CART_NUM = "[data-testid='cart-badge']"
    CART_BTN = "[data-testid='cart-button']"
    PRODUCT_NAME = "[data-testid='product-name']"
    PRODUCT_PRICE = "[data-testid='product-price']"

    # Cart product info
    CART_PRODUCT_NAME = "[data-testid='cart-line-name-classic-white-tee-mens']"
    CART_PRODUCT_PRICE = "[data-testid='cart-line-total-classic-white-tee-mens']"
    CART_PRODUCT_SIZE = "[data-testid^='cart-line-'] div:has-text('Size:') >> nth=0"
    CART_TOTAL_PRICE = "[data-testid='cart-drawer-total']"
    CHECK_OUT_BTN = "[data-testid='cart-drawer-checkout']"
    REMOVE_BTN = "[data-testid='cart-line-remove-classic-white-tee-mens']"
    EMPTY_CART_TIP = "[data-testid='cart-drawer-empty']"

    def is_add_to_cart_disabled(self):
        """Check if Add to Cart button is disabled"""
        try:
            self.wait_elem_visible(self.ADD_TO_CART_BTN)
            is_disabled = self.page.is_disabled(self.ADD_TO_CART_BTN)
            self.logger.info(f"Add to Cart button disabled status: {is_disabled}")
            return is_disabled
        except Exception as e:
            self.logger.error(f"Error checking button status: {str(e)}")
            raise e

    def add_to_cart(self):
        """
        Select size, increase quantity, add product to cart
        Returns: dictionary with product name, price, size, and cart badge count
        """
        try:
            self.wait_elem_visible(self.PRODUCT_NAME)
            self.wait_elem_visible(self.PRODUCT_PRICE)

            # Select product options and add to cart
            self.elem_click(self.SIZE_BTN)
            self.elem_click(self.ADD_NUM_BTN)
            self.elem_click(self.ADD_TO_CART_BTN)
            self.wait_elem_visible(self.CART_NUM)

            # Return all product info in a dictionary
            product_info = {
                "name": self.get_element_text(self.PRODUCT_NAME),
                "price": self.get_element_text(self.PRODUCT_PRICE),
                "size": self.get_element_text(self.SIZE_BTN),
                "cart_count": self.get_element_text(self.CART_NUM)
            }

            self.logger.info(f"Product added to cart: {product_info}")
            return product_info

        except Exception as e:
            self.logger.error(f"Failed to add product to cart: {str(e)}")
            raise e

    def cart_operation(self):
        """
        Open cart drawer and retrieve cart item information
        Returns: dictionary with cart item name, subtotal, size, total price
        """
        try:
            self.page.click(self.CART_BTN, force=True)
            self.wait_elem_visible(self.CART_PRODUCT_NAME)

            # Return cart information in a dictionary
            cart_info = {
                "name": self.get_element_text(self.CART_PRODUCT_NAME),
                "price": self.get_element_text(self.CART_PRODUCT_PRICE),
                "size": self.get_element_text(self.CART_PRODUCT_SIZE),
                "total": self.get_element_text(self.CART_TOTAL_PRICE)
            }

            self.logger.info(f"Cart information loaded: {cart_info}")
            return cart_info

        except Exception as e:
            self.logger.error(f"Cart operation failed: {str(e)}")
            raise e


    def go_to_checkout(self):
        """Click cart button and proceed to checkout page"""
        try:
            self.wait_elem_visible(self.CHECK_OUT_BTN)
            self.elem_click(self.CHECK_OUT_BTN)
            self.logger.info("Navigated to checkout page successfully")
        except Exception as e:
            self.logger.error(f"Failed to navigate to checkout: {str(e)}")
            raise e

    def clear_cart(self):
        """Clear cart items only if cart is not empty"""
        try:
            # Open cart drawer
            self.page.click(self.CART_BTN, force=True)
            self.page.wait_for_timeout(1000)

            # Check if cart is already empty
            if self.page.locator(self.EMPTY_CART_TIP).is_visible():
                self.elem_click(self.CART_BTN)
                self.logger.info("Cart is empty, no action needed")
                return

            # If cart not empty, remove item
            if self.page.locator(self.REMOVE_BTN).is_visible():
                self.elem_click(self.REMOVE_BTN)
                self.logger.info("Item removed from cart successfully")

            # Close cart drawer
            self.elem_click(self.CART_BTN)

        except Exception as e:
            self.logger.info("Clear cart skipped: " + str(e))
