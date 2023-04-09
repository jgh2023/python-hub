from time import sleep
from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("http://cdn1.python3.vip/files/selenium/test4.html")
driver.find_element_by_id("b1").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(5)
driver.quit()