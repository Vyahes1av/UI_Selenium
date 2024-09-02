import time
from conftest import driver
from data import Data
from locators import StellarburgerSearch
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestPersonalAccount:
    def test_transition_personal_account(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Input_name).send_keys(Data.Email_user)
        driver.find_element(*StellarburgerSearch.Input_password).send_keys(Data.Password_user)
        driver.find_element(*StellarburgerSearch.Button_logout).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))

        driver.find_element(*StellarburgerSearch.Button_personal_account).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Info_personal_account))
        element = driver.find_element(*StellarburgerSearch.Info_personal_account)
        assert element.text == 'В этом разделе вы можете изменить свои персональные данные'

    def test_transition_constructor(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Input_name).send_keys(Data.Email_user)
        driver.find_element(*StellarburgerSearch.Input_password).send_keys(Data.Password_user)
        driver.find_element(*StellarburgerSearch.Button_logout).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))

        driver.find_element(*StellarburgerSearch.Button_personal_account).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Info_personal_account))

        driver.find_element(*StellarburgerSearch.Button_constructor).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))
        element = driver.find_element(*StellarburgerSearch.Head_main)
        assert element.text == 'Соберите бургер'

    def test_exit_personal_account(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Input_name).send_keys(Data.Email_user)
        driver.find_element(*StellarburgerSearch.Input_password).send_keys(Data.Password_user)
        driver.find_element(*StellarburgerSearch.Button_logout).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))

        driver.find_element(*StellarburgerSearch.Button_personal_account).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Info_personal_account))

        driver.find_element(*StellarburgerSearch.Button_exit_personal_account).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))
        element = driver.find_element(*StellarburgerSearch.Head_personal_accoount)
        assert element.text in 'Вход'










