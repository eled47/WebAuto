import unittest 
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.youtube.com")
    
    def test_search_youtube(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        # mainPage.search_text_element = "pycon"
        mainPage.search_text_element = "EL47"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
