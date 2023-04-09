from time import sleep
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get(
    "http://authserver.cqsxedu.com/authserver/login?service=http%3A%2F%2Fehall.cqsxedu.com%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.cqsxedu.com%2Fnew%2Findex.html")
username = driver.find_element(By.ID, 'username')
username.send_keys("202118")
sleep(2)
username.send_keys(keys.Keys.CONTROL, 'a')
sleep(2)
username.send_keys(keys.Keys.CONTROL, 'c')
sleep(2)
username.send_keys(keys.Keys.BACK_SPACE)
password = driver.find_element(By.ID, "password")
password.send_keys(keys.Keys.CONTROL, 'v')
sleep(2)
driver.quit()
