from pages.base_page import BasePage
import logging


class HomePage(BasePage):
    logger = logging.getLogger(__name__)

    # Element locators
    HERO_HEADING = "h1:has-text('Goods')"
    BTN_SHOP_ALL = "[data-testid='hero-shop-cta']"
    FEATURED_PRODUCTS_LIST = "[data-testid='product-grid']"
    PRODUCT_CARDS = "[data-testid^='product-card-']"

    COOKIE_BANNER = "[data-testid='cookie-banner'], .cookie-banner, div:has-text('cookie')"
    COOKIE_BTN_ACCEPT_ALL = "#sp-accept"
    COOKIE_BTN_DECLINE = "#sp-decline"
    COOKIE_BTN_CUSTOMIZE = "#sp-customize"


    COOKIE_IFRAME = "#ifrmCookieBanner"

    def verify_homepage_loaded(self):
        """Verify all key homepage elements are loaded successfully"""
        try:
            self.logger.info("Starting homepage load verification")
            self.wait_elem_visible(self.HERO_HEADING)
            self.logger.info("Homepage loaded successfully")
            return self.get_element_text(self.HERO_HEADING)
        except Exception as e:
            self.logger.error(f"Homepage verification failed: {str(e)}")
            raise

    def click_shop_all(self):
        """Click 'Shop all products' button to navigate to product listing"""
        try:
            self.elem_click(self.BTN_SHOP_ALL)
            self.logger.info("Clicked 'Shop all products' successfully")
        except Exception as e:
            self.logger.error(f"Failed to click Shop All button: {str(e)}")
            raise

    def get_product_cards(self):
        """Get all product card elements from the homepage grid"""
        try:
            self.wait_elem_visible(self.PRODUCT_CARDS)
            self.logger.info("Product cards displayed")
            return self.find_elements(self.PRODUCT_CARDS)
        except Exception as e:
            self.logger.error(f"Failed to display product cards: {str(e)}")
            raise

    # Cookie iframe
    def is_cookie_banner_visible(self):
        """Verify cookie consent banner is displayed on page load (iframe)"""
        try:
            iframe = self.page.frame_locator(self.COOKIE_IFRAME)
            iframe.locator("body").wait_for(timeout=3000)
            self.logger.info("✅ Cookie banner displayed inside iframe")
            return True
        except Exception as e:
            self.logger.info("ℹ️ Cookie banner not present")
            return False

    def click_accept_all_cookies(self):
        """Click 'Accept all' button on cookie banner (iframe)"""
        try:
            iframe = self.page.frame_locator(self.COOKIE_IFRAME)
            iframe.locator(self.COOKIE_BTN_ACCEPT_ALL).click(timeout=3000)
            self.logger.info("✅ Clicked 'Accept all' cookies button")
        except Exception as e:
            self.logger.error(f"Failed to click Accept All cookies: {str(e)}")
            raise

    def click_decline_cookies(self):
        """Click 'Decline' button on cookie banner (iframe)"""
        try:
            iframe = self.page.frame_locator(self.COOKIE_IFRAME)
            iframe.locator(self.COOKIE_BTN_DECLINE).click(timeout=3000)
            self.logger.info("✅ Clicked 'Decline' cookies button")
        except Exception as e:
            self.logger.error(f"Failed to click Decline cookies: {str(e)}")
            raise

    def click_customize_cookies(self):
        """Click 'Customize' button on cookie banner (iframe)"""
        try:
            iframe = self.page.frame_locator(self.COOKIE_IFRAME)
            iframe.locator(self.COOKIE_BTN_CUSTOMIZE).click(timeout=3000)
            self.logger.info("✅ Clicked 'Customize' cookies button")
        except Exception as e:
            self.logger.error(f"Failed to click Customize cookies: {str(e)}")
            raise