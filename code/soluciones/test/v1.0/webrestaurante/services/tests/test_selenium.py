from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass() 
        PATH_WEB_DRIVER = r'C:\Users\Francisco\Downloads\chromedriver-win64\chromedriver.exe'
        cls.service = Service(PATH_WEB_DRIVER)
        cls.selenium = webdriver.Chrome(service=cls.service)
        cls.selenium.set_window_size(1200, 800)        

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_google(self):        
        browser = self.selenium
        url = "https://google.com"
        browser.get(url)                
        self.assertIn('Google', browser.title)
        caja = browser.find_element(By.ID, 'APjFqb')
        caja.send_keys("PERROS GIGANTES")
        time.sleep(1)
        caja.submit()    
        time.sleep(3)    