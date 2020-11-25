import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"

dropdown = Select(driver.find_element_by_name("ctl00$mainContent$ddl_originStation1"))
dropdown.select_by_visible_text("Goa (GOI)")


