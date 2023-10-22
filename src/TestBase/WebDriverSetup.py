from selenium import webdriver
import urllib3
import unittest

class WebDriverSetup(unittest.TestCase):
    
    #create an instance of webdriver with chrome and maximize the window.
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    # Close all tabs/windows and close the webdriver. 
    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
        