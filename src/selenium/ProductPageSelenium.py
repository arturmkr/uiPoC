from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ProductPageSelenium:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get("https://arturmkr.github.io/simple_web_site/products.html")
        return self

    def uhd_btn(self) -> WebElement:
        return self.driver.find_element_by_xpath("//*[text()='Select UHD']")
