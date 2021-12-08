from typing import List

import allure
from playwright.sync_api import Page, Locator, ElementHandle

from src.playwright.PageP import PageP


class ProductPageP(PageP):

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step
    def open(self):
        self.page.goto('https://arturmkr.github.io/simple_web_site/products.html')

    def product_inputs(self) -> List[ElementHandle]:
        return self.page.query_selector_all("div.boxCheckbox > input")

    def product_labels(self) -> List[ElementHandle]:
        return self.page.query_selector_all("div.box > div.boxLabel")

    def amount_selected_products(self) -> ElementHandle:
        return self.page.query_selector("span.selectedValue")

    def reset_btn(self) -> ElementHandle:
        return self.page.query_selector("//*[text()='Reset selection']")

    def uhd_btn(self) -> ElementHandle:
        return self.page.query_selector("//*[text()='Select UHD']")
