from time import sleep

from selenium import webdriver
driver =webdriver.Chrome()
driver.get("https://www.2345.com/web/innerBaiduSearch.html#/")
js ="window.scrollTo(0,1500)"
driver.execute_script(js)
sleep(2)
js1 ="window.scrollTo(0,2000)"
sleep(5)
driver.quit()