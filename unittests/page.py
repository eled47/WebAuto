from locator import MainPageLocators
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "search_query"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        # return "Python" in self.driver.title
        print(self.driver.title)
        return "YouTube" in self.driver.title
    
    def click_go_button(self):
        #the * separates a tuple into distinct objects
        #GO_BUTTON is the tuple (By.ID, "submit") in locator.py, so the * changes it to By.ID, "submit" as 2 separate objects
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source