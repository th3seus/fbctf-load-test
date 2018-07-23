from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

def view_navigation_menu(driver):
    """ returns navigation menu element to be used
    with other navigation functions """
    menu = driver.find_element_by_css_selector(".nav-left")
    return menu

def view_tutorial(driver):
    """ opens up and steps through tutorial """
    nav = view_navigation_menu(driver)
    tutorial = driver.find_element_by_css_selector(".fb-init-tutorial")
    tutPages = 8

    actions = ActionChains(driver)
    actions.move_to_element(nav)
    time.sleep(2)
    actions.click(tutorial)
    actions.perform()
    while tutPages != 0:
        time.sleep(2)
        nextBtn = driver.find_element_by_css_selector(".cta--yellow")
        actions.move_to_element(nextBtn)
        time.sleep(2)
        actions.click(nextBtn)
        actions.perform()
        tutPages -= 1

driver = webdriver.Firefox()
user = "team1"
password = "password3"

# go to homepage 
driver.get("https://54.193.2.111/index.php")
assert "Facebook CTF" in driver.title

# login
team_login(driver, user, password)

WebDriverWait(driver, 10).until(EC.title_contains("Facebook CTF | Gameboard"))
assert "Facebook CTF | Gameboard" in driver.title, "not loaded properly"

view_tutorial(driver)

""" try:
    view_tutorial(driver)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Skip to play")))
finally:
    print "finally"
    time.sleep(15)
    driver.close() """

