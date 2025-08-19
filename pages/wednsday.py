from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class WedPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.CSS_SELECTOR, "#header-search-form-val") # wednsday
        self.serch_btn = (By.CSS_SELECTOR, "#header-search-form > button")
        self.video_btn = (By.CSS_SELECTOR, "#app > div.grid-cell.grid-col-main > div:nth-child(3) > section > div.video-list > div:nth-child(1) > div.item-info > h5 > a")
        self.maximize_btn = (By.CSS_SELECTOR, "#oframeplayer > pjsdiv:nth-child(21) > pjsdiv:nth-child(3)")
        self.parameters_btn = (By.CSS_SELECTOR, "#oframeplayer > pjsdiv:nth-child(19) > pjsdiv:nth-child(3)")
        self.qual_btn = (By.CSS_SELECTOR, "#player_settings > pjsdiv > pjsdiv:nth-child(1)")
        self.better_qual_btn = (By.CSS_SELECTOR, "#player_settings > pjsdiv > pjsdiv:nth-child(5)")
        self.qual_back_btn = (By.CSS_SELECTOR, "#player_settings > pjsdiv > pjsdiv:nth-child(4)")
        self.play_btn = (By.CSS_SELECTOR, "#oframeplayer > pjsdiv:nth-child(3) > video")

    def enter_search_input(self, search_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.search_input)).send_keys(search_input)

    def click_serch_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.serch_btn)).click()

    def click_video_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.video_btn)).click()

    def click_maximize_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.maximize_btn)).click()

    def click_parameters_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.parameters_btn)).click()

    def click_qual_btn (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.qual_btn)).click()

    def click_better_qual_btn (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.better_qual_btn)).click()

    def click_qual_back_btn (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.qual_back_btn)).click()

    def click_play_btn (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.play_btn)).click()

