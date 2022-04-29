from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:

    quantityDropdown = "select[name='quantity']"
    selectQuantity = ''

    def __init__(self, driver: webdriver):
        self.driver = driver

    def changeQuantity(self):
        wait = WebDriverWait(self.driver, 3)
        self.selectQuantity = Select(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.quantityDropdown))))
        self.selectQuantity.select_by_value("2")


