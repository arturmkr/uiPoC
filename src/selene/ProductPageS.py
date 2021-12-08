import allure
from selene import Browser
from selene.core.entity import SeleneElement, SeleneCollection

from src.selene.PageS import PageS


class ProductPageS(PageS):

    def __init__(self, browser: Browser):
        super().__init__(browser)

    @allure.step
    def open(self):
        self.browser.open("/products.html")
        return self

    def uhd_btn(self) -> SeleneElement:
        return self.browser.element("//*[text()='Select UHD']")

    def reset_btn(self) -> SeleneElement:
        return self.browser.element("//*[text()='Reset selection']")

    def amount_selected_products(self) -> SeleneElement:
        return self.browser.element("span.selectedValue")

    def product_labels(self) -> SeleneCollection:
        return self.browser.all("div.box > div.boxLabel")

    def product_inputs(self) -> SeleneCollection:
        return self.browser.all("div.box > div.boxCheckbox")
