from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

import logging
logging.basicConfig(filename="test_report.log", level=logging.INFO, format="%(asctime)s - %(message)s")

USERNAME = "sadershape"
PASSWORD = "damir231564"

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)
driver.get("https://github.com/login")

driver.implicitly_wait(10)

logging.info("Navigated to GitHub login page.")
time.sleep(2)  

driver.find_element(By.ID, "login_field").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "commit").click()
time.sleep(3)  

try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Open user navigation menu']"))
    )
    logging.info("Login successful.")
except TimeoutException:
    logging.error("Login failed.")
    driver.save_screenshot("debug_login_failed.png")
    driver.quit()
    exit()

profile_button = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Open user navigation menu']"))
)
actions = ActionChains(driver)
actions.move_to_element(profile_button).click().perform()
logging.info("Profile menu opened successfully.")
time.sleep(2) 

wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
side_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'prc-Dialog-Dialog-luvDS')]")))
time.sleep(2)  

settings_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/settings/profile']"))
)
settings_link.click()
logging.info("Navigated to Settings successfully.")
time.sleep(3) 

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
logging.info("Navigated to Selenium test page.")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)  

time.sleep(2)  

try:
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "my-select"))
    )
    select = Select(select_element)
    select.select_by_visible_text("Two")
    logging.info("Dropdown selection successful.")
except TimeoutException:
    logging.error("Dropdown selection failed.")


# ✅ Test Report: Save logs & ensure cleanup
logging.info("Test execution completed. Closing browser.")
driver.quit()
