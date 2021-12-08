from selene import have, query
from selene.support.conditions import be

from src.selene.ProductPageS import ProductPageS


def test_uhd_count_shows_correct_amount_selene(browser_selene):
    product_page = ProductPageS(browser_selene)

    product_page.open()
    product_page.uhd_btn().click()

    uhd_labels = [label for label in product_page.product_labels() if "UHD" in label.get(query.text)]
    product_page.amount_selected_products().should(have.exact_text(str(len(uhd_labels))))


def test_can_select_uhd_tv_selene(browser_selene):
    product_page = ProductPageS(browser_selene)

    product_page.open()
    product_page.uhd_btn().click()

    for label, checkbox in zip(product_page.product_labels(), product_page.product_inputs()):
        if "UHD" in label.get(query.text):
            checkbox.should(be.selected)
