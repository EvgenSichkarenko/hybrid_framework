from selenium.webdriver.common.by import By

from base.base import BaseDriver


class SearchFlight(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FILTER_ONE = "//p[@class='font-lightgrey bold'][normalize-space()='1']"

    def get_filter_one(self):
        return self.driver.find_element(By.XPATH, self.FILTER_ONE)

    def choose_search(self):
        self.get_filter_one().click()
