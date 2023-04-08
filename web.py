from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(10)
login = driver.find_element_by_link_text("登录").click()
driver.find_element(By.ID, "TANGRAM__PSP_11__changePwdCodeItem").click()
a = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName'and @ name='userName']")
a.click()
a.send_keys("13506212493")
password = driver.find_element_by_xpath("//*[@type='password' and @name='password']")
password.click()
password.send_keys("202118Jgh")
Login = driver.find_element_by_xpath(
    "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit' ]").click()
driver.implicitly_wait(8)
start = driver.find_element_by_xpath("//*[@class='vcode-spin-button' and @id='vcode-spin-button149' ]")
end = driver.find_element_by_xpath("//*[@class='vcode-spin-bottom-tips slideShine'and@id='vcode-spin-bottom-tips149' ]")
action = ActionChains(driver)
action.drag_and_drop(start, end)
action.perform()
sleep(10)
driver.quit()
