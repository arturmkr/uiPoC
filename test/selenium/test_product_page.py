from src.selenium.ProductPageSelenium import ProductPageSelenium


def test_uhd_count_shows_correct_amount_selenium(browser_selenium):
    product_page = ProductPageSelenium(browser_selenium)

    product_page.open()
    product_page.uhd_btn().click()
