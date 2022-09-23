from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['--headless'])
options.add_experimental_option('excludeSwitches', ['--no-sandbox'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://demo.midtrans.com/")
driver.maximize_window
driver.find_element(By.LINK_TEXT,"BUY NOW").click()
wait = WebDriverWait(driver, 10)
checkout = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'cart-checkout')))
time.sleep(3)
checkout.click()
time.sleep(3)
driver.switch_to.frame("snap-midtrans")
time.sleep(3)
ccard = driver.find_element(By.CLASS_NAME,"promo-banner-text")
ccard.click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "card-number-input-container").click()
driver.find_element(By.CLASS_NAME,"valid-input-value").send_keys("4811111111111114")
driver.find_element(By.ID,"card-expiry").send_keys("0223")
driver.find_element(By.ID,"card-cvv").send_keys("123")
driver.find_element(By.CLASS_NAME, "card-pay-button-part").click()
print("OK")
