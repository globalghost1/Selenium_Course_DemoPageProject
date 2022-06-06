import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager
from page_object_pattern.pages.Search_Hotel import SearchHotelPage
from page_object_pattern.pages.SearchResults import SearchResultsPage

from Page_Object_Pattern.Test.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().instal())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("12/09/2019","13/09/2019")
        search_hotel_page.set_travellers("2", "2")
        search_hotel_page.perform.search()
        result_page = SearchResultsPage(self.driver)
        hotels_names = result_page.get_hotel_prices()
        price_values = result_page.get_hotel_prices()

        assert hotels_names[0] == 'Jumeirah Beach Hotel'
        assert hotels_names[1] == 'Oasis Beach Tower'
        assert hotels_names[2] == 'Rose Rayhaan Rotana'
        assert hotels_names[3] == 'Hyatt Regency Perth'
        assert price_values[0] == '$22'
        assert price_values[1] == '$50'
        assert price_values[2] == '$80'
        assert price_values[3] == '$150'


