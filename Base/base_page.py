from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_element_exist(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def switch_to_new_window(self):
        current_window_handle = self.driver.current_window_handle
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != current_window_handle:
                self.driver.switch_to.window(handle)
                break

    def get_current_url(self):
        return self.driver.current_url

    def check_url_contains(self, expected_url):
        current_url = self.get_current_url()
        if expected_url in current_url:
            return True
        else:
            return False
