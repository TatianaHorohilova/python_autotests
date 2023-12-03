import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_product_view_sku():
    """
    Test case WERT-1
    """

chrome_options = Options()
chrome_options.add_argument("start-maximized") # открываем на полный экран
chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
chrome_options.add_argument("--disable-extensions") # отключаем расширения
# chrome_options.add_argument("--headless")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url="https://testqastudio.me/")

element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
element.click()

element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
element.click()
sku = driver.find_element(By.CLASS_NAME, value="sku")
assert sku.text == 'BFB9ZOK210', "Unexpected sku"