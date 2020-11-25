from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
childwindow = driver.window_handles[1]
parentwindow = driver.window_handles[0]
driver.switch_to.window(childwindow)
driver.find_element_by_tag_name("h3")
print(driver.find_element_by_tag_name("h3").text)
driver.switch_to.window(parentwindow)
print(driver.find_element_by_tag_name("h3").text)