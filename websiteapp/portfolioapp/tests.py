from websiteapp.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowsePortfolioTests(Browser):
    """ Tests for portfolio.html and project.html"""

    def test_portfolio(self):
        """ tests for portfolio page"""
        self.selenium.get("".join([self.live_server_url, "/portfolio/"]))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual("Portfolio", header_title.text)
        links = self.selenium.find_elements_by_css_selector(
            "#header_portfolio li a")
        self.assertEqual(len(links), 3)
        self.assertEqual(links[0].text, "Catégorie 1")
        self.assertEqual(links[1].text, "Catégorie 2")
        self.assertEqual(links[2].text, "Catégorie 3")
        # main
        categories = self.selenium.find_elements_by_css_selector(
            "#main_portfolio .container")
        self.assertEqual(len(categories), 3)

        def assert_project_in_category(category, number_cards):
            projects = category.find_elements_by_class_name(
                "card")
            self.assertEqual(len(projects), number_cards)
        # Category 1
        assert_project_in_category(categories[0], 5)
        # Category 2
        assert_project_in_category(categories[1], 1)
        # Category 3
        assert_project_in_category(categories[2], 2)
        # Link to project
        links = categories[0].find_elements_by_tag_name("a")
        links[3].click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "header_project")))
        self.assertEqual(
            "http://localhost:12345/portfolio/5/", self.selenium.current_url)

    def test_project(self):
        """ tests for project page"""
        self.selenium.get("".join([self.live_server_url, "/portfolio/4/"]))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual("Catégorie 1", header_title.text)
        project_title = self.selenium.find_element_by_tag_name("h3")
        self.assertEqual("Projet 4", project_title.text)
        # main
        main_title = self.selenium.find_element_by_tag_name("h5")
        self.assertEqual("Le 4e projet", main_title.text)
        self.selenium.find_element_by_link_text("Site Web").click()
        WebDriverWait(self.selenium, 10).until(
            EC.number_of_windows_to_be(2))
        default_handle = self.selenium.current_window_handle
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "pg-index")))
        self.assertIn("DuckDuckGo", self.selenium.title)
        self.selenium.close()
        self.selenium.switch_to_window(default_handle)
