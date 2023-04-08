from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.cqsxedu.com/email.jsp?urltype=tree.TreeTempUrl&wbtreeid=1061")
public = driver.find_element_by_link_text("公共服务")
action = ActionChains(driver)
action.move_to_element(public)
action.perform()
sleep(8)
driver.quit()
