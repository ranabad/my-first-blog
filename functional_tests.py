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
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn("Profile", header_text)
        header_text2 = self.browser.find_element_by_tag_name('h3').text 
        self.assertIn("Education", header_text2)
        paragraph_search=self.browser.find_elements_by_tag_name('p')
        class_contentcontainer=self.browser.find_elements_by_class_name('content-container')
        

        


if __name__ == '__main__':  
    unittest.main(warnings='ignore')
