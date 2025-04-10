from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)
driver.get("https://github.com/login")

driver.implicitly_wait(10)

driver.find_element(By.ID, "login_field").send_keys("your_username")
driver.find_element(By.ID, "password").send_keys("your_password")
driver.find_element(By.NAME, "commit").click()

try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//summary[@aria-label='View profile and more']"))
    )
    print("Login successful.")
except TimeoutException:
    print("Login failed or took too long.")

profile_icon = driver.find_element(By.XPATH, "//summary[@aria-label='View profile and more']")
actions = ActionChains(driver)
actions.move_to_element(profile_icon).perform()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
settings_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/settings/profile']")))
settings_link.click()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
select_element = driver.find_element(By.NAME, "my-select")
select = Select(select_element)
select.select_by_visible_text("Two")

try:
    assert "GitHub" in driver.title
    print("[PASS] Title contains 'GitHub'")
except AssertionError:
    print("[FAIL] Title does not contain 'GitHub'")

time.sleep(3)
driver.quit()
