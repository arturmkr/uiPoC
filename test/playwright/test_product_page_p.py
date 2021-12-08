from src.playwright.ProductPageP import ProductPageP


def test_uhd_count_shows_correct_amount_playwright(browser_playwright):
    page = browser_playwright.new_page()
    product_page = ProductPageP(page)

    product_page.open()
    product_page.uhd_btn().click()

    uhd_labels = [label for label in product_page.product_labels() if "UHD" in label.inner_text()]
    assert product_page.amount_selected_products().inner_text() == str(len(uhd_labels))


def test_can_select_uhd_tv_playwright(browser_playwright):
    page = browser_playwright.new_page()
    product_page = ProductPageP(page)

    product_page.open()
    product_page.uhd_btn().click()

    for label, checkbox in zip(product_page.product_labels(), product_page.product_inputs()):
        if "UHD" in label.inner_text():
            assert checkbox.is_checked()
        else:
            assert not checkbox.is_checked()
