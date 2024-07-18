from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_page import BasePage


class JobPage(BasePage):
    SEE_ALL_JOBS = (By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")
    FILTER_LOCATION_CONTAINER = "//*[@id='select2-filter-by-location-container']"
    FILTER_LOCATION_OPTION = "//*[@id='filter-by-location']/option[2]"
    FILTER_DEPARTMENT_CONTAINER = "//*[@id='select2-filter-by-department-container']"
    FILTER_DEPARTMENT_OPTION = "//*[@id='filter-by-department']/option[17]"
    VIEW_ROLE_BUTTONS = (By.XPATH, "//a[text()='View Role']")

    def click_see_all_jobs(self):
        self.wait_element_clickable(self.SEE_ALL_JOBS).click()

    def filter_location(self, expected_title):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.FILTER_LOCATION_CONTAINER)))

        location_filter = self.driver.find_element(By.XPATH, self.FILTER_LOCATION_CONTAINER)
        location_title_value = location_filter.get_attribute("title")

        if not location_title_value == expected_title:
            location_filter.click()
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.FILTER_LOCATION_OPTION)))
            self.driver.find_element(By.XPATH, self.FILTER_LOCATION_OPTION).click()
        else:
            pass

    def filter_department(self, expected_title):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.FILTER_DEPARTMENT_CONTAINER)))

        department_filter = self.driver.find_element(By.XPATH, self.FILTER_DEPARTMENT_CONTAINER)
        department_filter_title_value = department_filter.get_attribute("title")

        if not department_filter_title_value == expected_title:
            department_filter.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.FILTER_DEPARTMENT_OPTION)))
            self.driver.find_element(By.XPATH, self.FILTER_DEPARTMENT_OPTION).click()
        else:
            pass

    def click_view_role_button(self):
        button_view_role = self.driver.find_elements(*self.VIEW_ROLE_BUTTONS)
        ActionChains(self.driver).move_to_element(button_view_role[1]).click().perform()
        WebDriverWait(self.driver, 10)
