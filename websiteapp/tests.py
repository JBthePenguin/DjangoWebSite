from websiteapp.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowseBaseIndexTests(Browser):
    """ Tests for base.html and index.html"""

    def test_navbar(self):
        """ tests for nav bar"""
        self.selenium.get(self.live_server_url)
        # title
        self.assertEqual(self.selenium.title, "Django Website | Accueil")
        # nav links
        nav_links = self.selenium.find_elements_by_css_selector(
            "nav.navbar .nav-link"
        )
        self.assertEqual(len(nav_links), 5)

        def assert_click_nav_link(ind_link, header_id):
            """assert link redirection"""
            nav_links = self.selenium.find_elements_by_css_selector(
                "nav.navbar .nav-link")
            nav_links[ind_link].click()
            WebDriverWait(self.selenium, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "".join(["header_", header_id]))))
            if header_id == "index":
                self.assertEqual(
                    "http://localhost:12345/",
                    self.selenium.current_url)
            else:
                self.assertIn(
                    "".join(["/", header_id, "/"]),
                    self.selenium.current_url)

        def assert_link_color(ind_link):
            """ assert active link color """
            nav_links = self.selenium.find_elements_by_css_selector(
                "nav.navbar .nav-link")
            other_links = []
            for x in range(5):
                if x == ind_link:
                    pass
                else:
                    other_links.append(x)
            self.assertNotEqual(
                nav_links[other_links[0]].value_of_css_property("color"),
                nav_links[ind_link].value_of_css_property("color"))
            self.assertEqual(
                nav_links[other_links[0]].value_of_css_property("color"),
                nav_links[other_links[1]].value_of_css_property("color"),
                nav_links[other_links[2]].value_of_css_property("color"),)
            self.assertEqual(
                nav_links[other_links[0]].value_of_css_property("color"),
                nav_links[other_links[3]].value_of_css_property("color"),)
        # Index
        assert_click_nav_link(0, "index")
        assert_link_color(0)
        # About
        assert_click_nav_link(1, "about")
        assert_link_color(1)
        # Portfolio
        assert_click_nav_link(2, "portfolio")
        assert_link_color(2)
        # Blog
        assert_click_nav_link(3, "blog")
        assert_link_color(3)
        # Contact
        assert_click_nav_link(4, "contact")
        assert_link_color(4)

    def test_footer(self):
        """ tests for footer"""
        self.selenium.get(self.live_server_url)
        # change color of theme
        # light color
        self.selenium.find_element_by_css_selector("footer .toggle").click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bg-light")))
        nav_links = self.selenium.find_elements_by_css_selector(
            "nav.navbar .nav-link")
        self.assertEqual(
            nav_links[1].value_of_css_property("color"), "rgba(0, 0, 0, 0.5)")
        # dark color
        self.selenium.find_element_by_css_selector("footer .toggle").click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bg-dark")))
        footer = self.selenium.find_element_by_tag_name("footer")
        self.assertEqual(
            footer.value_of_css_property("color"), "rgb(255, 255, 255)")

        # change language
        def checkboxe():
            checkboxes = self.selenium.find_elements_by_css_selector(
                "footer .toggle")
            checkboxes[1].click()
        # english
        checkboxe()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "About")))
        page_title = self.selenium.title
        self.assertEqual(page_title, "Django Website | Home")
        # french
        checkboxe()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Mentions légales")))
        footer_text = self.selenium.find_element_by_css_selector("footer i")
        self.assertEqual(footer_text.text, "Suivez-moi:")

    def test_index(self):
        """ tests for index page"""
        self.selenium.get(self.live_server_url)
        # title
        self.assertEqual(self.selenium.title, "Django Website | Accueil")
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Accueil")
        # main
        links = self.selenium.find_elements_by_css_selector(
            "#main_index div a h4")
        self.assertEqual(len(links), 4)

        # links
        def assert_click_link(ind_link, header_id):
            """ assert redirection of links and come back to home page"""
            links = self.selenium.find_elements_by_css_selector(
                "#main_index div a h4")
            links[ind_link].click()
            WebDriverWait(self.selenium, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "".join(["header_", header_id]))))
            self.assertEqual(
                "".join(["http://localhost:12345/", header_id, "/"]),
                self.selenium.current_url)
            self.selenium.find_element_by_class_name("fa-home").click()
            WebDriverWait(self.selenium, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "header_index")))
        # About
        assert_click_link(0, "about")
        # Portfolio
        assert_click_link(1, "portfolio")
        # Blog
        assert_click_link(2, "blog")
        # Contact
        assert_click_link(3, "contact")
