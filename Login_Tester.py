from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/login")

#Enter username
driver.find_element(By.ID, "username").send_keys("tomsmith")

#Enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

#Click login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()



#Wait for the result message to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "flash")))



#check result message
message = driver.find_element(By.ID, "flash").text
print("Login Result:", message)

#Close the browser
driver.quit()