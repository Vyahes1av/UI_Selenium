import time
from conftest import driver
from data import Data
from locators import StellarburgerSearch
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestRegistration:

    def test_new_user_reg(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))
        driver.find_element(*StellarburgerSearch.Button_reg).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_reg_page))

        time.sleep(3)

        driver.find_element(*StellarburgerSearch.Input_reg_name).send_keys(Data.Reg_name_user)
        driver.find_element(*StellarburgerSearch.Input_reg_email).send_keys(Data.Reg_email_user)
        driver.find_element(*StellarburgerSearch.Input_reg_password).send_keys(Data.Reg_password_user)
        time.sleep(3)
        driver.find_element(*StellarburgerSearch.Button_reg_new_user).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(StellarburgerSearch.Head_reg_page))
        element = driver.find_element(*StellarburgerSearch.Head_reg_page)
        assert element.is_displayed()

    def test_false_password(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))
        driver.find_element(*StellarburgerSearch.Button_reg).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_reg_page))

        time.sleep(3)

        driver.find_element(*StellarburgerSearch.Input_reg_name).send_keys(Data.Reg_name_user)
        driver.find_element(*StellarburgerSearch.Input_reg_email).send_keys(Data.Reg_email_user)
        driver.find_element(*StellarburgerSearch.Input_reg_password).send_keys(Data.Reg_password_false)
        driver.find_element(*StellarburgerSearch.Button_reg_new_user).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(StellarburgerSearch.Head_reg_page))
        element = driver.find_element(*StellarburgerSearch.False_reg_password)
        assert element.text == "Некорректный пароль"
