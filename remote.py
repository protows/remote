# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
    	self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, command_executor='http://127.0.0.1:4444/wd/hub')

        
    def test_search_in_python_org(self):
    	driver = self.driver
    	driver.get("https://www.google.co.uk/")
    	print(driver.title)

    def tearDown(self):
    	self.driver.close()

if __name__ == "__main__":
	unittest.main()