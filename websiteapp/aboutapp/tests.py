from websiteapp.browser_selenium import Browser


class BrowseAboutTests(Browser):
    """ Tests for about.html """

    def test_about(self):
        """ tests for about page"""
        self.selenium.get("".join([self.live_server_url, "/about/"]))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(
            "".join(["à".upper(), " propos"]), header_title.text)
        # main
        divs = self.selenium.find_elements_by_css_selector(
            "#main_about div")
        self.assertEqual(len(divs), 2)
        # services
        services = self.selenium.find_elements_by_css_selector(
            "#main_about #services li")
        self.assertEqual(len(services), 3)
        # skills
        skills = self.selenium.find_elements_by_css_selector(
            "#main_about #skills li")
        self.assertEqual(len(skills), 3)
