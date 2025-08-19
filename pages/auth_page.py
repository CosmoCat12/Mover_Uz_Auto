from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_btn = (By.CSS_SELECTOR, "#top-panel > div:nth-child(5) > a")
        self.login_input = (By.CSS_SELECTOR, "#modal-user-login-username")
        self.password_input = (By.CSS_SELECTOR, "#modal-user-login-password")
        self.submit_btn = (By.CSS_SELECTOR, "#modal-user-login-form > div:nth-child(5) > button")

    def click_login_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def enter_login_input(self, login_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login_input)).send_keys(login_input)

    def enter_password_input(self, password_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password_input)

    def click_submit_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.submit_btn)).click()