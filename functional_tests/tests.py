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
browser = webdriver.Firefox()
try:
   
    browser.get('https://ranabad.pythonanywhere.com/cv')
  
    print(browser.title) 
    html = browser.page_source
    time.sleep(10)
    print(str(html))

finally:
    browser.quit()
    display.stop() 

if __name__ == '__main__':  
    unittest.main(warnings='ignore')    
