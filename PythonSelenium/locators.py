
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Prabodh")
driver.find_element_by_css_selector("input[name='email']").send_keys("prabodh@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("training123$")
driver.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_xpath("//@div[class='form-group']/label")
driver.find_element_by_css_selector("input[value='Submit']").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#print(driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text)

message = driver.find_element_by_css_selector("[class*='alert-success']").text #alternate method for above line
assert "success" in message

driver.close()