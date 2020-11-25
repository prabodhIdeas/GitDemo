from selenium import webdriver

#Chrome_options = webdriver.ChromeOptions()
#Chrome_options.add_argument("--start-maximized")
#Chrome_options.add_argument("ignore certificate errors")
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path= "D:\\browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*=shop]").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.execute_script('window.scrollTo(0,0);')
driver.find_element_by_css_selector("a[class*='btn-primary']").click()

checkedoutitem = driver.find_element_by_css_selector("h4[class='media-heading'] a").text

assert "Blackberry" in checkedoutitem
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
Successmsg = driver.find_element_by_xpath("//div[@class= 'alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in Successmsg
driver.get_screenshot_as_file("test1.png")


