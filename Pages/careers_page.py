import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Base.base_page import BasePage

logging.basicConfig(filename='uygulama.log', level=logging.INFO, format='%(message)s - %(asctime)s')


class CareersPage(BasePage):
    CHECK_LOCATIONS = (By.XPATH, "/html/body/div[1]/section[1]/div/div/div/div[1]/div/h2")
    CHECK_LIFE_AT_INSIDER = (By.XPATH, "/html/body/div[1]/section[4]/div/div/div/div[1]/div/h2")
    CHECK_TEAMS = (By.XPATH, "//*[@id='career-find-our-calling']/div/div/div[1]/h3")
    SEE_ALL_TEAMS_BUTTON = (By.XPATH, "//a[contains(@class, 'loadmore') and contains(text(), 'See all teams')]")

    def check_locations(self):
        try:
            self.wait_element_exist(self.CHECK_LOCATIONS)
            logging.info("Location bolumu sayfa uzerinde var.")
        except NoSuchElementException:
            logging.info("Location bolumu sayfa uzerinde bulunamadi.")

    def check_life_at_insider(self):
        try:
            self.wait_element_exist(self.CHECK_LIFE_AT_INSIDER)
            logging.info("Life At Insider bolumu sayfa uzerinde var.")
        except NoSuchElementException:
            logging.info("Life At Insider bolumu sayfa uzerinde bulunamadi.")

    def check_teams(self):
        try:
            self.wait_element_exist(self.CHECK_TEAMS)
            logging.info("Teams  bolumu sayfa uzerinde var.")
        except NoSuchElementException:
            logging.info("Teams bolumu sayfa uzerinde bulunamadi.")

    def click_see_all_teams(self):
        self.wait_element_clickable(self.SEE_ALL_TEAMS_BUTTON).click()

    def scroll_down(self):
        self.wait_element_exist(self.SEE_ALL_TEAMS_BUTTON)
        self.wait_element_exist(self.CHECK_LIFE_AT_INSIDER)
        scroll_step = 50
        see_all_teams_button = self.driver.find_element(By.XPATH,
                                                        "//a[contains(@class, 'loadmore') and contains(text(), 'See all teams')]")
        life_at_insider = self.driver.find_element(By.XPATH, "/html/body/div[1]/section[4]/div/div/div/div[1]/div/h2")
        current_position = see_all_teams_button.location['y']
        while current_position < life_at_insider.location['y']:
            self.driver.execute_script(f"window.scrollBy(0, {scroll_step});")
            current_position += scroll_step
            time.sleep(0.1)
