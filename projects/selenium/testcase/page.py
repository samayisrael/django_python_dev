from locator import *
from element import BasePageElement

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class SearchTextElement(BasePageElement):
    locator = 'q'

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return 'Python' in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    def is_results_found(self):
        return 'No Results found.' not in self.driver.page_source
