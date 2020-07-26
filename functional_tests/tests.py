import time

from django.test import LiveServerTestCase
from selenium import webdriver

from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
try:
   
    browser = webdriver.Firefox()
    browser.get('http://www.ranabad.pythonanywhere.com')
  
    assertIn('Personal Blog', browser.title)  
        html = browser.page_source
        time.sleep(10)
        print(html)

finally:
    
    browser.quit()
    display.stop() 

       

        
        


