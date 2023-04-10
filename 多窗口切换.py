from time import sleep
from selenium import webdriver
driver =webdriver.Chrome()
driver.get("https://www.baidu.com/?tn=88093251_42_hao_pg")
news =driver.find_element_by_link_text("新闻")
news.click()
hadles =driver.window_handles
print(hadles)
driver.switch_to.window(hadles[-1])
selectw =driver.find_element_by_xpath("//*[@class='word' and @id ='ww']")
selectw.send_keys("123456")

sleep(4)
driver.quit()