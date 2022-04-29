from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BooksPage:
    firstBookOfNews = 'ul.a-unordered-list.a-nostyle.a-horizontal.octopus-pc-card-list.octopus-pc-card-height-v3 li'
    addToCartButton = '[name="submit.add-to-cart"]'
    showCart = '#nav-cart-count-container'

    def __init__(self, driver: webdriver):
        self.driver = driver

    def selectFirstBookOfNews(self):
        self.driver.find_element(By.CSS_SELECTOR, self.firstBookOfNews).click()

    def addToCart(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.addToCartButton))).click()

    def goToCart(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.showCart))).click()
