from realbrowserlocusts import FirefoxLocust, ChromeLocust, PhantomJSLocust
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from locust import TaskSet, task


def open_ctf_index(self):
    self.client.get("https://13.57.214.36/index.php")
    self.client.wait.until(EC.title_is("Facebook CTF"))

def open_rules_page(self):
    self.client.find_element_by_link_text("rules").click()
    self.client.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fb-glitch')), "Rules page is visible")

def open_login_page(self):
    self.client.find_element_by_link_text("Login").click()
    self.client.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fb-glitch')), "Login page is visible")

def login_as_team(self, user, password):
    open_ctf_index(self)
    time.sleep(5)
    open_login_page(self)
    self.client.find_element_by_name("team_name").send_keys(user)
    self.client.find_element_by_name("password").send_keys(password)

    self.client.find_element_by_id("login_buttom").click()

class CTFTeamBehavior(TaskSet):

    def on_start(self):
        self.client.timed_event_for_locust("Click to", "login", login_as_team(self, "team1", "password3"))


"""    @task(1)
    def homepage_and_docs(self):
        self.client.timed_event_for_locust("Go to", "homepage", self.open_locust_homepage)
        self.client.timed_event_for_locust("Click to", "documentation", self.click_through_to_documentation)
"""


class CTFTeam(FirefoxLocust):
#class LocustUser(ChromeLocust):
#class LocustUser(PhantomJSLocust):

#    host = "not really used"
    timeout = 30 #in seconds in waitUntil thingies
    min_wait = 100
    max_wait = 1000
    screen_width = 1200
    screen_height = 600
    task_set = CTFTeamBehavior