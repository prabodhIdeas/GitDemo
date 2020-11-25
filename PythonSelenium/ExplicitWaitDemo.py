import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")

list = []
list2 = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")
time.sleep(4)
Total = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert Total ==3
Items = driver.find_elements_by_css_selector("div[class='product-action'] button")
#traversing from child to Grand parent class using Xpath
for item in Items:
    list.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()
#print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
Wait = WebDriverWait(driver, 7)
Wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
checkout = driver.find_elements_by_css_selector("p.product-name")
for check in checkout:
    list2.append(check.text) #sending items in lis
#print(list2)
assert list == list2 #validating selected items and check out items are similar
originalAmount = driver.find_element_by_class_name("discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
Wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
AfterDiscount = driver.find_element_by_class_name("discountAmt").text
assert float(AfterDiscount) < int(originalAmount) # validate discounted price is less than actual
print(driver.find_element_by_class_name("promoInfo").text)

amounts = (driver.find_elements_by_xpath("//tr/td[5]/p"))
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

#TotalAmnt = driver.find_element_by_class_name("totAmt").text
#assert sum == int(TotalAmnt)