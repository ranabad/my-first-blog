"""I wont test whether Post Method works because USER MUST BE ADMIN (ME)
  
    so functional test shows that browser can load up cv page it checks that button to link works for user and

    it prints out for vistors that are not the admin(ME) the basic html 
    
    page and what contains to make sure they can see CV items 

    I test the functional test with my pythonpythonanywhere console"""  
import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()
        display.stop() 

    def test_can_user__can_and__view_cv_page(self):  
       self.browser.get('https://ranabad.pythonanywhere.com')
       inputbox = self.browser.find_element_by_link_text('CV')
       inputbox.send_keys(Keys.ENTER)
       self.assertIn('https://ranabad.pythonanywhere.com/cv',self.browser.current_url)
       self.browser.get('https://ranabad.pythonanywhere.com/cv')
       self.assertIn("Rana's Personal Blog", self.browser.title)
       html = self.browser.page_source
       print(html)
       

if __name__ == '__main__':  
    unittest.main(warnings='ignore')    
