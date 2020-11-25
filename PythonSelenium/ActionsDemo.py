from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver) #to perform hover actions in web browser
Hover = driver.find_element_by_id("mousehover")
action.move_to_element(Hover).perform() #perform needs to be written to perform any action with actions class
childbutton = driver.find_element_by_link_text("Reload")
action.move_to_element(childbutton ).click().perform()