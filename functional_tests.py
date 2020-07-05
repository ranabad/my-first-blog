from selenium import webdriver
import unittest




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
        input = self.browser.find_element_by_id('Rana AL Badrani')  
       
    


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  


   

