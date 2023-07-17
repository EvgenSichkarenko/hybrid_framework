import unittest
from test_data.test_dat import flights
from pages.launching_page import LaunchPage
import time
import pytest


@pytest.mark.usefixtures("setup")
class TestDemo:

    # @pytest.fixture(autouse=True)
    # def setup_method(self):
    #     self.lp = LaunchPage(self.driver)
        # self.ut = Utils()

    @pytest.mark.parametrize("going_from, going_to, date", flights)
    def test_demo_exp(self, going_from, going_to, date):
        self.lp = LaunchPage(self.driver)
        sf = self.lp.search_flights(going_from, going_to, date)
        self.lp.page_scroll()
        sf.choose_search()

    def test_one(self):
        print("hello")
        time.sleep(10)

    def test_two(self):
        time.sleep(10)

    def test_three(self):
        time.sleep(10)

    def test_four(self):
        time.sleep(10)

    def test_five(self):
        time.sleep(10)

    def test_six(self):
        time.sleep(10)

