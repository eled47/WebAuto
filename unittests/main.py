import unittest 
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
    
    # from 7:06 in the Python Selenium Tutorial #5 on Tech With Tim start function with test if you 
    # want it to function as a test
    def test_example(self):
        print("Test")
        assert True

    def tearDown(self):
        self.driver.close()
