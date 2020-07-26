"""I wont test whether Post Method works because USER MUST BE ADMIN (ME)
  
    so functional test shows that browser can load up cv page 

    it prints out for vistors that are not the admin(ME) the basic html 
    
    page and what contains to make sure they can see CV items 

    I test the functional test with my pythonpythonanywhere console"""  
import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver

from pyvirtualdisplay import Display


display = Display(visible=0, size=(800, 600))
display.start()
class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()
        display.stop() 

    def test_can_start_show_cv_page(self):  
       self.browser.get('https://ranabad.pythonanywhere.com/cv')
  
        self.assertIn("Rana's Personal Blog", self.browser.title)
        html = browser.page_source
        time.sleep(10)
          print(str(html))

if __name__ == '__main__':  
    unittest.main(warnings='ignore')    
