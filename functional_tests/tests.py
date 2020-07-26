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
