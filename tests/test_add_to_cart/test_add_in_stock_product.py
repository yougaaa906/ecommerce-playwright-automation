import logging
from pages.product_detail_page import ProductDetailPage

logger = logging.getLogger(__name__)

@pytest.mark.xfail(reason="Intentional test - System calculates total with shipping fee")
def test_add_to_cart_and_verify_cart_details(base_page, navigate_to_in_stock_product):
    """Verify cart count, item info and price calculation after adding product"""
    logger.info("Starting test: Add to cart and verify all cart details")

    # Add product to cart
    product_detail = ProductDetailPage(base_page)
    product_info = product_detail.add_to_cart()

    # Verify cart badge count
    assert product_info["cart_count"] == "2", \
        f"Expected cart count: 2, Actual: {product_info['cart_count']}"

    # Open cart and get cart info
    cart_info = product_detail.cart_operation()

    # Verify product name and size
    assert product_info["name"] == cart_info["name"], "Product name mismatch"
    assert product_info["size"] in cart_info["size"], "Product size mismatch"

    # Verify price calculation
    unit_price = float(product_info["price"].replace("$", ""))
    expected_subtotal = unit_price * 2
    cart_subtotal = float(cart_info["price"].replace("$", ""))
    cart_total = float(cart_info["total"].replace("$", ""))

    assert cart_subtotal == expected_subtotal, "Incorrect subtotal"
    assert cart_total == cart_subtotal, "Total does not match subtotal"

    logger.info("Test passed: All cart validations completed successfully")
