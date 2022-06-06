import pytest
from webdrivermanager import ChromeDriverManager
from selenium import webdriver


@pytest.fixture()
def setup(self):
    driver = webdriver.Chrome(ChromeDriverManager().instal())
    driver.implicity_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    self.driver.quit()