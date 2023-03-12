import time

from selenium.webdriver.common.by import By
from selenium import webdriver


class CustomerPage:

    link_main_customers_xpath="//div[@class='os-content']//ul[contains(@class,nav-sidebar)]//i[contains(@class,'user')]//following-sibling::p[contains(text(),'Customers')]"
    link_sub_customers_xpath= "//div[@class='os-content']//ul[contains(@class,nav-sidebar)]//a[contains(@href,'List')]//following-sibling::p[contains(text(),'Customers')]"
    text_search_email_xpath ="//input[@id='SearchEmail']"
    button_search_xpath = "//button[@id='search-customers']"
    text_search_result_email_xpath = "//table[@id='customers-grid']//tr[@class='odd']//td[2]"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_customers(self):
        self.driver.find_element(By.XPATH,self.link_main_customers_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.link_sub_customers_xpath).click()
        time.sleep(2)

    def search_email(self,email):
        self.driver.find_element(By.XPATH,self.text_search_email_xpath).send_keys(email)
        time.sleep(2)

    def click_search(self):
        self.driver.find_element(By.XPATH,self.button_search_xpath).click()
        time.sleep(3)

    def validate_search_result(self):
        return self.driver.find_element(By.XPATH,self.text_search_result_email_xpath).text

