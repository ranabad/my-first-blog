import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Safari()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page(self):    
        self.browser.get('http://ranabad.pythonanywhere.com')
        self.assertIn('Personal Blog', self.browser.title) 
           
    def test_can_get_cv_page(self):  
        self.browser.get('http://ranabad.pythonanywhere.com/cv')
        

        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a new skill'
        )

        

       
        inputbox.send_keys('django')  
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: django' for row in rows)
        )


        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list
    


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
