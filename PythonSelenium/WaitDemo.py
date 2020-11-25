import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")
time.sleep(4)
Total = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert Total == 3
Items = driver.find_elements_by_css_selector("div[class='product-action'] button")
for item in Items:
    item.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_class_name("promoInfo").text)
