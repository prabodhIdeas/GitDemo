from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") != "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobutton = driver.find_elements_by_name("radioButton")
radiobutton[2].click()
assert radiobutton[2].is_selected()
