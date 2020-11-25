from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Hello")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

ShopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script('arguments[0].click();', ShopButton)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') # to scroll down in webpage
