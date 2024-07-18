from selenium.webdriver.common.by import By
from Base.base_page import BasePage


class HomePage(BasePage):
    COOKIES_ACCEPT = (By.XPATH, "//*[@id='wt-cli-accept-all-btn']")
    COMPANY_NAVIGATE = (By.XPATH, "//*[@id='navbarNavDropdown']/ul[1]/li[6]")
    CAREERS_NAVIGATE = (By.XPATH, "//*[@id='navbarNavDropdown']/ul[1]/li[6]/div/div[2]/a[2]")

    def accept_cookies(self):
        self.wait_element_clickable(self.COOKIES_ACCEPT).click()

    def navigate_to_company(self):
        self.wait_element_clickable(self.COMPANY_NAVIGATE).click()

    def navigate_to_careers(self):
        self.wait_element_clickable(self.CAREERS_NAVIGATE).click()
