from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import time

def team_login(driver, user, password):
    """ team login using username and password """
    login = driver.find_element_by_link_text("Login")
    login.click()

    # submit creds
    driver.find_element_by_name("team_name").send_keys(user)
    driver.find_element_by_name("password").send_keys(password)

    # find login button and submit
    login = driver.find_element_by_id("login_button")
    login.click()


driver = webdriver.Firefox()
user = "team1"
password = "password3"

# go to homepage 
driver.get("https://13.57.214.36/index.php")
assert "Facebook CTF" in driver.title

# login
team_login(driver, user, password)

WebDriverWait(driver, 10).until(EC.title_contains("Facebook CTF | Gameboard"))
assert "Facebook CTF | Gameboard" in driver.title, "not loaded properly"
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.highlighted:nth-child(131)")))

finally:
    country = driver.find_element_by_css_selector("g.highlighted:nth-child(131)")
    country.click()