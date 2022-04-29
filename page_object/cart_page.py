from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:

    modifyQuantity = 'span.a-button-text.a-declarative'
    quantityDropdown = ''

    def __init__(self, driver: webdriver):
        self.driver = driver

    def changeQuantity(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.modifyQuantity))).click()
        self.quantityDropdown = Select(self.driver.find_elements(By.CSS_SELECTOR, 'select[name="quantity"]'))
        self.quantityDropdown.select_by_value("2")
li[aria-labelledby="quatity_2"]

