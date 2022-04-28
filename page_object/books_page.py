from selenium import webdriver
from selenium.webdriver.common.by import By


class BooksPage:
    firstBookOfNews = ''

    def __init__(self, driver: webdriver):
        self.driver = driver


    def selectFirstBookNouveautes(self):
        self.driver.find_element(By.CSS_SELECTOR, self.firstBookOfNews).click()


