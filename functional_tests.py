import time
import unittest

from django.test import TestCase
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_page_and_retrieve(self):
        #I wont test whether Post Method works because USER MUST BE ADMIN (ME)
        self.browser.get('http://127.0.0.1:8000/cv')
        self.assertIn('Personal Blog', self.browser.title)  
        html = self.browser.page_source
        time.sleep(2)
        print(html)

        


if __name__ == '__main__':  
    unittest.main(warnings='ignore')
