from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    cookie_button_selector = "#sp-cc-accept"
    hamburguer_menu_selector = "#nav-hamburger-menu"
    side_menu_selector = "#hmenu-canvas"
    books_menu_selector = "a[data-menu-id='10']"
    allBooksButton = "ul.hmenu-visible li:nth-of-type(3)"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def closeCookies(self):
        self.driver.find_element(By.CSS_SELECTOR, self.cookie_button_selector).click()

    def openAllMenu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.hamburguer_menu_selector).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.side_menu_selector)))

    def openBookCategory(self):
        self.driver.find_element(By.CSS_SELECTOR, self.books_menu_selector).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, self.books_menu_selector)))
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.allBooksButton)))

    def openAllBooks(self):
        self.driver.find_element(By.CSS_SELECTOR, self.allBooksButton).click()

