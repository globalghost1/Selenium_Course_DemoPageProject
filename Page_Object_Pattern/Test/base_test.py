import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager


class BaseTest:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().instal())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()
