from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class Browser(StaticLiveServerTestCase):
    """ Browser for the tests"""
    port = 12345
    fixtures = [
        "page_fixtures.json", "footer_fixtures.json",
        "social_fixtures.json", "alert_fixtures.json",
        "button_fixtures.json", "placeholder_fixtures.json",
        "aboutapp_fixtures.json", "portfolioapp_fixtures.json",
        "blogapp_fixtures.json", "contact_fixtures.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
