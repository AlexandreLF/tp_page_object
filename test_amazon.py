from selenium import webdriver


def test_amazon():
    driver = webdriver.Chrome()
    driver.get("https://amazon.fr/")
    driver.maximize_window()
    driver.quit()