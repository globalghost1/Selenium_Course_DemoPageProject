import logging

from page_object_pattern.locators.locators import SearchHotelLocators
from selenium.webdriver.common.by import By

class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        #self.search_hotel_span_xpath = "//span[text()] = 'Search by Hotel or City Name"
        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        #self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        #self.location_match_xpath = "//span[text()='Dubai']"
        self.location_match_xpath = SearchHotelLocators.location_match_xpath
        #self.check_in_input_name = "checkin"
        self.check_in_input_name = SearchHotelLocators.check_in_input_name
        #self.check_out_input_name = "checkout"
        self.check_out_input_name = SearchHotelLocators.check_out_input_name
        #self.travellers_input_id = "travellersInput"
        self.travellers_input_id = SearchHotelLocators.travellers_input_id
        #self.adult_input_id = "adultInput"
        self.adult_input_id = SearchHotelLocators.adult_input_id
        #self.child_input_id = "childInput"
        self.child_input_id = SearchHotelLocators.child_input_id
        #self.search_button_xpath = "//button[text()='Search']"
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element(By.XPATH, self.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in [checkin] and [checkout] dates".format(checkin=check_in, checkout=check_out))
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys(check_out)

    def set_travellers(self, adults, child):
        set.logger.info("Setting travellers adults - [adults] and child - [kids]".format(adults=adults, kids=child))
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adult_input_id).clear()
        self.driver.find_element(By.ID, self.adult_input_id).send_keys(adults)
        self.driver.find_element(By.ID, self.child_input_id_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(child)

    def perform_search(self):
        set.logger.info("Performing search")
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()




        # driver.find_element(By.XPATH, "//span[text()] = 'Search by Hotel or City Name']").click()
        # driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys('Dubai')
        # driver.find_element(By.XPATH, "//span[text()='Dubai']").click()
        # Ustawienie dat zameldowania i wymeldowania
        # driver.find_element(By.NAME, "checkin").send_keys("12/09/2019")
        # driver.find_element(By.NAME, "checkout").send_keys("13/09/2019")
        # Druga możliwość wprowadzenia zameldowania i wymeldowania
        # driver.find_element(By.NAME, "checkin").click()
        # driver.find_element(By.XPATH, "//td[@class='day' and text()='13'").click()
        # elementy = driver.find_element(By.XPATH, "//td[@class='day' and text()='15'").click()
        # for element in elementy:
        # if (element.is_displayed()):
        #  element.click()
        #  break
        # Ustawienie ilości podróżnych i wyszukiwanie wyników
        # driver.find_element(By.ID, "travellersInput").click()
        # driver.find_element(By.ID, "adultInput").clear()
        # driver.find_element(By.ID, "adultInput").send_keys("4")
        # driver.find_element(By.ID, "childInput").clear()
        # driver.find_element(By.ID, "childInput").send_keys("4")
        # driver.find_element(By.XPATH, "//[text()='Search']").click()
