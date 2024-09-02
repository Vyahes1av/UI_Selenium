import time
from conftest import driver
from data import Data
from locators import StellarburgerSearch
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestConsructor:
    def test_buns(self, driver):
        driver.find_element(*StellarburgerSearch.Button_chapter_sauces).click()
        time.sleep(3)
        driver.find_element(*StellarburgerSearch.Button_chapter_buns).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Input_name_buns))
        element = driver.find_element(*StellarburgerSearch.Input_name_buns)
        assert element.text == 'Краторная булка N-200i'

    def test_sauces(self, driver):
        driver.find_element(*StellarburgerSearch.Button_chapter_sauces).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Input_name_sauses))
        element = driver.find_element(*StellarburgerSearch.Input_name_sauses)
        assert element.text == 'Соус традиционный галактический'

    def test_fillings(self, driver):
        driver.find_element(*StellarburgerSearch.Button_chapter_fillings).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(StellarburgerSearch.Input_name_fillings))
        element = driver.find_element(*StellarburgerSearch.Input_name_fillings)
        assert element.text == 'Говяжий метеорит (отбивная)'