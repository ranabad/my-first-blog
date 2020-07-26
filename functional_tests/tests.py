import time

from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):  

    def setUp(self):  
        self.browser = webdriver.Safari

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_page_and_retrieve(self):
        #I wont test whether Post Method works because USER MUST BE ADMIN (ME)
        #so functional test shows that browser can load up cv page 
        # it prints out for vistors that are not the admin(ME) the basic html page and what contains to make sure they can see CV items
        self.browser.get(self.live_server_url)
        self.assertIn('Personal Blog', self.browser.title)  
        html = self.browser.page_source
        time.sleep(10)
        print(html)

        