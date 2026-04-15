from pages.base_page import BasePage
from config.config import *
import logging


class CheckoutPage(BasePage):
    logger = logging.getLogger(__name__)

    # Shipping Address Locators
    SHIP_NAME = "[data-testid='ship-name']"
    SHIP_ADDRESS1 = "[data-testid='ship-address1']"
    SHIP_ADDRESS2 = "[data-testid='ship-address2']"
    SHIP_CITY = "[data-testid='ship-city']"
    SHIP_ZIP = "[data-testid='ship-zip']"
    SHIP_COUNTRY = "[data-testid='ship-country']"

    # Payment Locators
    PAY_NAME = "[data-testid='pay-name']"
    PAY_NUMBER = "[data-testid='pay-number']"
    PAY_EXPIRY = "[data-testid='pay-expiry']"
    PAY_CVC = "[data-testid='pay-cvc']"

    # Order Summary & Action Locators
    SUMMARY_SUBTOTAL = "[data-testid='summary-subtotal'] > span:nth-child(2)"
    SUMMARY_SHIPPING = "[data-testid='summary-shipping'] > span:nth-child(2)"
    SUMMARY_TOTAL = "[data-testid='cart-total']"
    PLACE_ORDER_BTN = "[data-testid='place-order']"
    ORDER_SUCCESS_MSG = "h1:has-text('Thank you')"

    def fill_all_checkout_info(self):
        try:
            self.wait_elem_visible(self.SHIP_NAME)
            self.elem_input(self.SHIP_NAME, CHECKOUT_FULL_NAME)
            self.elem_input(self.SHIP_ADDRESS1, CHECKOUT_ADDRESS1)
            self.elem_input(self.SHIP_ADDRESS2, CHECKOUT_ADDRESS2)
            self.elem_input(self.SHIP_CITY, CHECKOUT_CITY)
            self.elem_input(self.SHIP_ZIP, CHECKOUT_ZIP)
            self.elem_input(self.SHIP_COUNTRY, CHECKOUT_COUNTRY)

            self.elem_input(self.PAY_NAME, CHECKOUT_CARDHOLDER)
            self.elem_input(self.PAY_NUMBER, CHECKOUT_CARD_NUMBER)
            self.elem_input(self.PAY_EXPIRY, CHECKOUT_EXPIRY)
            self.elem_input(self.PAY_CVC, CHECKOUT_CVC)

            self.logger.info("All checkout information filled successfully")

        except Exception as e:
            self.logger.error(f"Failed to fill checkout information: {str(e)}")
            raise e

    def get_order_summary(self):
        try:
            self.wait_elem_visible(self.SUMMARY_TOTAL)
            summary = {
                "subtotal": self.get_element_text(self.SUMMARY_SUBTOTAL),
                "shipping": self.get_element_text(self.SUMMARY_SHIPPING),
                "total": self.get_element_text(self.SUMMARY_TOTAL)
            }
            self.logger.info(f"Order summary loaded: {summary}")
            return summary
        except Exception as e:
            self.logger.error(f"Failed to retrieve order summary: {str(e)}")
            raise e

    def place_order(self):
        try:
            self.wait_elem_clickable(self.PLACE_ORDER_BTN)
            self.elem_click(self.PLACE_ORDER_BTN)
            self.wait_elem_visible(self.ORDER_SUCCESS_MSG)
            success_message = self.get_element_text(self.ORDER_SUCCESS_MSG)
            self.logger.info(f"Order placed successfully: {success_message}")
            return success_message
        except Exception as e:
            self.logger.error(f"Failed to place order: {str(e)}")
            raise e