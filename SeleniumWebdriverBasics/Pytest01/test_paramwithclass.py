import pytest
# from selenium.webdriver.chrome import webdriver
from selenium import webdriver

driver = None
@pytest.fixture(params=["chrome","firefox"],scope="class")
def init_browser(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param =="firefox":
        driver=webdriver.Firefox()
    request.cls.driver = driver
    driver.get("http://google.com")
    driver.maximize_window()
    yield
    driver.close()
# @pytest.mark.usefixtures("init_browser")
# class BaseTest:
#     pass

@pytest.mark.usefixtures("init_browser")
class Test_Google():

    def test_google_title(self):
        # self.driver.get("http://google.com")
        title=self.driver.title
        assert title=="Google"



