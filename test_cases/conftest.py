from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure
from allure import attachment_type
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def setup(request):
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Remote(
    #     command_executor='http://localhost:4444',
    #     options=webdriver.ChromeOptions()
    # )
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


# allure report
# pytest --browser chrome --alluredir=reports/report
# allre serve reports/report
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    # marker = item.get_closest_marker("ui")
    # if marker:
    if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
        try:
            allure.attach(item.instance.driver.get_screenshot_as_png(),
                          name=item.name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
