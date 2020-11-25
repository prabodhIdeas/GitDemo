
from selenium import webdriver
#browser exposed an executable file
#Through selenium test we need to invoke executable file which wil then invoke the actual browser
#driver = webdriver.Chrome(executable_path="D:\\browsers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="D:\\browsers\geckodriver.exe")
driver.get("https://www.youtube.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get("https://www.youtube.com/watch?v=yoqVzN7Lxt0")
driver.back()
driver.minimize_window()
driver.refresh()
driver.close()