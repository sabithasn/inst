from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the browser (make sure to have the appropriate web driver)
driver = webdriver.Chrome()

# Go to Instagram
driver.get("https://www.instagram.com")

# Log in (you need to fill in your username and password)
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')
username_input.send_keys('YOUR_USERNAME')
password_input.send_keys('YOUR_PASSWORD')
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for login to complete

# Search for "Amrita"
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys('Amrita')
time.sleep(2)
search_box.send_keys(Keys.RETURN)
search_box.send_keys(Keys.RETURN)  # Press enter again to go to the profile page

time.sleep(5)  # Wait for the page to load

# Scrape data (this is a simplistic example)
profiles = driver.find_elements(By.XPATH, "//a[contains(@href,'/')]")
for profile in profiles:
    print(profile.get_attribute('href'))

# Don't forget to close the browser
driver.quit()
