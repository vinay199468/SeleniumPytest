# from selenium.webdriver.common.by import By
# import allure
# from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest


@pytest.fixture(params=["chrome","firefox"], scope="function")
def get_browser(request):
    remote_url="http://localhost:4444/wd/hub"
    if request.param == "chrome":
        driver = webdriver.Remote(command_executor=remote_url,options=webdriver.ChromeOptions())
    if request.param == "firefox":
        driver = webdriver.Remote(command_executor=remote_url,options=webdriver.FirefoxOptions())

    driver.get("https://www.facebook.com")
    driver.maximize_window()
    yield driver
    driver.quit()