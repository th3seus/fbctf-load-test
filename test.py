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

    # find nav bar, then click the link to open tutorial
    actions = ActionChains(driver)
    actions.move_to_element(nav)
    time.sleep(2)
    actions.click(tutorial)
    actions.perform()

    # step through tutorial pages
    for x in range(0,9):
        print "at window %d" % x
        time.sleep(2)
        nextBtn = False
        while nextBtn == False:
            nextBtn = False
            nextBtn = WebDriverWait(driver, 3).until(find_tutorial_next_button)
            print nextBtn
            if EC.staleness_of(nextBtn) == False:
                actions.move_to_element(nextBtn)
                time.sleep(2)
                actions.click(nextBtn)
                time.sleep(2)
                actions.perform()
                # tutPages -= 1
            else:
                nextBtn = False

def find_tutorial_next_button(driver):
    print 'looking for button'
    btn = driver.find_element_by_css_selector(".cta--yellow")
    if btn:
        print "found button"
        return btn
    else:
        print 'did not find button'
        return False

driver = webdriver.Firefox()
user = "team1"
password = "password3"

# go to homepage 
driver.get("https://52.53.207.37/index.php")
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
