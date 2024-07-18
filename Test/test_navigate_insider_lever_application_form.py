import unittest
import logging
from selenium.webdriver import Chrome
from Base.base_page import BasePage
from Pages.home_page import HomePage
from Pages.careers_page import CareersPage
from Pages.job_page import JobPage
from Base.database_utils import save_test_result

logging.basicConfig(level=logging.INFO)


class TestNavigateInsiderLeverApplicationForm(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome()
        self.base_page = BasePage(self.driver)
        self.driver.get("https://useinsider.com/")
        self.driver.maximize_window()

    def test_navigate_insider_lever_application_form(self):

        home_page = HomePage(self.driver)
        home_page.accept_cookies()
        logging.info("Cookies kabul edildi.")
        home_page.navigate_to_company()
        logging.info("Company sekmesine basildi.")
        home_page.navigate_to_careers()
        logging.info("Careers sayfasina gidildi.")

        careers_page = CareersPage(self.driver)
        careers_page.check_locations()
        careers_page.check_life_at_insider()
        careers_page.check_teams()
        careers_page.click_see_all_teams()
        careers_page.scroll_down()
        logging.info("Careers sayfasindaki butun adimlar tamamlandi.")

        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        job_page = JobPage(self.driver)
        logging.info("Quality Assurance sayfasina gidildi.")
        job_page.click_see_all_jobs()
        job_page.filter_location("Istanbul, Turkey")
        job_page.filter_department("Quality Assurance")
        logging.info("Is ilanlanlari belirlenen ozelliklere gore listelendi.")
        job_page.click_view_role_button()

        self.base_page.switch_to_new_window()
        final_url = "https://jobs.lever.co/useinsider/49d9cb7f-3c19-4fbe-9975-4b46847f18d4"
        if self.base_page.check_url_contains(final_url):
            logging.info("Test Basarili: Butun adimlar tamamlandi ve lever sayfasına ulasildi.")
            test_result = "SUCCESS"
        else:
            logging.error(
                f"Test Basarisiz: Beklenen lever sayfasi acilamadi. Alinan URL: " + self.base_page.get_current_url())
            test_result = "FAILED"

        save_test_result(test_result)
        logging.info("Test sonucu veritabanına kaydedildi.")
    def tearDown(self):
        self.driver.quit()
