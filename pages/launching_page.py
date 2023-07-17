import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base import BaseDriver
from pages.search_flight_page import SearchFlight


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM = "input[id='BE_flight_origin_city']"
    GOING_TO = "input[id='BE_flight_arrival_city']"
    GOING_TO_RESULTS = "//div[@class='viewport']//li"
    DEPARTURE_DATE = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody/tr"
    WEEKEND = "//td[@class=' weekend']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def get_depart_from_element(self):
        return self.wait_element_is_clickable(By.CSS_SELECTOR, self.DEPART_FROM)

    def get_going_to_element(self):
        return self.wait_element_is_clickable(By.CSS_SELECTOR, self.GOING_TO)

    def get_depart_dates(self):
        return self.wait_presence_of_all_elements_located(By.XPATH, self.GOING_TO_RESULTS)

    def get_depart_date(self):
        return self.wait_element_is_clickable(By.XPATH, self.DEPARTURE_DATE)

    def get_all_dates(self):
        return self.wait_element_is_clickable(By.XPATH, self.ALL_DATES)

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def depart_from(self, from_dp):
        self.get_depart_from_element().click()
        self.get_depart_from_element().send_keys(from_dp)
        time.sleep(1)
        self.get_depart_from_element().send_keys(Keys.ENTER)
        time.sleep(1)

    def going_to(self, going):
        self.get_going_to_element().click()
        time.sleep(1)
        self.get_going_to_element().send_keys(going)
        search_results = self.get_depart_dates()
        time.sleep(1)
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                break

    def select_date(self, select_date):
        self.get_depart_date().click()
        all_dates = self.get_all_dates().find_elements(By.XPATH, self.WEEKEND)
        time.sleep(1)
        for date in all_dates:
            if date.get_attribute("data-date") == select_date:
                date.click()
                break

    def click_search(self):
        self.get_search_button().click()
        time.sleep(6)

    def search_flights(self, from_dp, going_to, select_date):
        self.depart_from(from_dp)
        self.going_to(going_to)
        self.select_date(select_date)
        self.click_search()
        sf = SearchFlight(self.driver)
        return sf
