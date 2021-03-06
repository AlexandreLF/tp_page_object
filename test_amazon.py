import selenium

from page_object.home_page import HomePage
from page_object.books_page import BooksPage
from page_object.cart_page import CartPage
from selenium import webdriver


def test_amazon():
    driver = webdriver.Chrome()
    driver.get("https://amazon.fr/")
    driver.maximize_window()
    driver.quit()


def test_amazon1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr/")

    driver.quit()

def test_page_object():
    # Arrange
    excpetedQuantity = '2'

    # Act
    driver = selenium.webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr/")

    homePage = HomePage(driver)
    homePage.closeCookies()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()

    booksPage = BooksPage(driver)
    booksPage.selectFirstBookOfNews()
    booksPage.addToCart()
    booksPage.goToCart()

    cartPage = CartPage(driver)
    cartPage.changeQuantity()

    # Assert
    assert excpetedQuantity == cartPage.selectQuantity.first_selected_option.text

    driver.quit()
