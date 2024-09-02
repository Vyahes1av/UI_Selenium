import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
time.sleep(3)
WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
time.sleep(3)
driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Регистрация']")))
time.sleep(3)
driver.find_element(By.NAME, "name").send_keys("ЛюбительБургеров")
time.sleep(3)
driver.find_element(By.XPATH, "//fieldset[2]//input[@name='name']").send_keys("burgerlove@burg.com")
time.sleep(3)
driver.find_element(By.NAME, "Пароль").send_keys("333666Bg!")
time.sleep(3)
driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
time.sleep(3)

driver.quit()