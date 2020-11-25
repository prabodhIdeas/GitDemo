from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")#to switch to frame; iframe; frameset
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("it worked!!!")
driver.switch_to.default_content() #to switch back to default html
print(driver.find_element_by_tag_name("h3").text)