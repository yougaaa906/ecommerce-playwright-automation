import logging
from pages.checkout_page import CheckoutPage
from pages.product_detail_page import ProductDetailPage

logger = logging.getLogger(__name__)


def test_complete_checkout_flow_validation(logged_in_page, navigate_to_checkout_page):

    base_page = logged_in_page
    checkout_page = CheckoutPage(base_page)

    summary = checkout_page.get_order_summary()
    subtotal = float(summary["subtotal"].replace("$", ""))
    shipping = float(summary["shipping"].replace("$", ""))
    total = float(summary["total"].replace("$", ""))

    assert total == round(subtotal + shipping, 2)

    checkout_page.fill_all_checkout_info()
    success_msg = checkout_page.place_order()
    assert "success" in success_msg.lower() or "placed" in success_msg.lower()

    logger.info("Test passed: Full checkout flow completed successfully")
