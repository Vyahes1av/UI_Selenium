import time
from conftest import driver
from data import Data
from locators import StellarburgerSearch
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestEntrence:

    def test_button_logout(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Input_name).send_keys(Data.Email_user)
        driver.find_element(*StellarburgerSearch.Input_password).send_keys(Data.Password_user)
        driver.find_element(*StellarburgerSearch.Button_logout).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))
        element = driver.find_element(*StellarburgerSearch.Head_main)
        assert element.text == 'Соберите бургер'

    def test_button_personal_account(self, driver):
        driver.find_element(*StellarburgerSearch.Button_personal_account).click()
        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Input_name).send_keys(Data.Email_user)
        driver.find_element(*StellarburgerSearch.Input_password).send_keys(Data.Password_user)
        driver.find_element(*StellarburgerSearch.Button_logout).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))
        element = driver.find_element(*StellarburgerSearch.Head_main)
        assert element.text == 'Соберите бургер'

    def test_reg_form_log(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))
        driver.find_element(*StellarburgerSearch.Button_reg).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_reg_page))

        time.sleep(3)
        driver.find_element(*StellarburgerSearch.Button_logout_form_reg).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Input_name).send_keys(Data.Email_user)
        driver.find_element(*StellarburgerSearch.Input_password).send_keys(Data.Password_user)
        driver.find_element(*StellarburgerSearch.Button_logout).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))
        element = driver.find_element(*StellarburgerSearch.Head_main)
        assert element.text == 'Соберите бургер'

    def test_password_recovery(self, driver):
        driver.find_element(*StellarburgerSearch.Button_login_page).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Button_password_recovery).click()

        time.sleep(3)

        WebDriverWait(driver,5).until(ec.presence_of_element_located(StellarburgerSearch.Head_password_recovery))

        driver.find_element(*StellarburgerSearch.Button_password_recovery_login).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_personal_accoount))

        driver.find_element(*StellarburgerSearch.Input_name).send_keys(Data.Email_user)
        driver.find_element(*StellarburgerSearch.Input_password).send_keys(Data.Password_user)
        driver.find_element(*StellarburgerSearch.Button_logout).click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Head_main))
        element = driver.find_element(*StellarburgerSearch.Head_main)
        assert element.text == 'Соберите бургер'
