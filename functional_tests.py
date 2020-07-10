from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/cv')

        # She notices the page title and header mention to-do lists
        self.assertIn('Personal Blog', self.browser.title)  



        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Rana's Personal Blog", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_tag_name('h3').text 
        self.assertIn("Education", inputbox)

        

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        




         

       

if __name__ == '__main__':  
    unittest.main(warnings='ignore')