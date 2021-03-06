# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestLucho():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lucho(self):
    # Test name: lucho
    # Step # | name | target | value | comment
    # 1 | open | http://newtours.demoaut.com/ |  | 
    self.driver.get("http://newtours.demoaut.com/")
    # 2 | setWindowSize | 760x694 |  | 
    self.driver.set_window_size(760, 694)
    # 3 | click | name=userName |  | 
    self.driver.find_element(By.NAME, "userName").click()
    # 4 | type | name=userName | tutorial | 
    self.driver.find_element(By.NAME, "userName").send_keys("tutorial")
    # 5 | type | name=password | tutorial | 
    self.driver.find_element(By.NAME, "password").send_keys("tutorial")
    # 6 | sendKeys | name=password | ${KEY_ENTER} | 
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    # 7 | click | name=fromPort |  | 
    self.driver.find_element(By.NAME, "fromPort").click()
    # 8 | select | name=fromPort | label=London | 
    dropdown = self.driver.find_element(By.NAME, "fromPort")
    dropdown.find_element(By.XPATH, "//option[. = 'London']").click()
    # 9 | click | css=tr:nth-child(4) > td > select > option:nth-child(3) |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td > select > option:nth-child(3)").click()
    # 10 | click | name=toPort |  | 
    self.driver.find_element(By.NAME, "toPort").click()
    # 11 | select | name=toPort | label=Paris | 
    dropdown = self.driver.find_element(By.NAME, "toPort")
    dropdown.find_element(By.XPATH, "//option[. = 'Paris']").click()
    # 12 | click | css=tr:nth-child(6) option:nth-child(5) |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) option:nth-child(5)").click()
    # 13 | click | css=input:nth-child(4) |  | 
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").click()
    # 14 | click | name=findFlights |  | 
    self.driver.find_element(By.NAME, "findFlights").click()
    # 15 | click | name=reserveFlights |  | 
    self.driver.find_element(By.NAME, "reserveFlights").click()
    # 16 | click | name=passFirst0 |  | 
    self.driver.find_element(By.NAME, "passFirst0").click()
    # 17 | type | name=passFirst0 | luciano | 
    self.driver.find_element(By.NAME, "passFirst0").send_keys("luciano")
    # 18 | type | name=passLast0 | olivera | 
    self.driver.find_element(By.NAME, "passLast0").send_keys("olivera")
    # 19 | click | name=creditnumber |  | 
    self.driver.find_element(By.NAME, "creditnumber").click()
    # 20 | type | name=creditnumber | 123456 | 
    self.driver.find_element(By.NAME, "creditnumber").send_keys("123456")
    # 21 | click | name=buyFlights |  | 
    self.driver.find_element(By.NAME, "buyFlights").click()
    # 22 | click | linkText=SIGN-OFF |  | 
    self.driver.find_element(By.LINK_TEXT, "SIGN-OFF").click()
  
