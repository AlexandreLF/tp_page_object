from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage:

    modifyQuantity = 'span.a-button-text.a-declarative'
    quantityDropdown = ''

    def __init__(self, driver: webdriver):
        self.driver = driver

    def changeQuantity(self):
        self.driver.find_element(By.CSS_SELECTOR, self.modifyQuantity).click()
        self.quantityDropdown = Select(self.driver.find_elements(By.CSS_SELECTOR, 'select[name="quantity"]'))
        self.quantityDropdown.select_by_value("2")