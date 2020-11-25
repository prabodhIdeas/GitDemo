
from selenium import webdriver

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--start-minimized")
Chrome_options.add_argument("headless")
Chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe",options= Chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)