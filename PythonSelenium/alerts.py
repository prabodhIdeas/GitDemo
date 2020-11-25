from selenium import webdriver
variable1 = "Prabodh"
driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Prabodh")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alert.text
assert variable1 in alert.text
alert.accept()