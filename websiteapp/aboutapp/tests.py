import os
from websiteapp.browser_selenium import Browser
from websiteapp.aboutapp.models import Term, AboutCategory
from websitedjango.settings import BASE_DIR


class BrowseAboutTests(Browser):
    """ Tests for about.html """

    def test_about(self):
        """ tests for about page"""
        self.selenium.get("".join([self.live_server_url, "/about/"]))
        # title
        self.assertEqual(self.selenium.title, "Django Website|À propos")
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(
            "".join(["À propos"]), header_title.text)
        # main
        divs = self.selenium.find_elements_by_css_selector(
            "#main_about .container")
        self.assertEqual(len(divs), 2)
        # services
        services = self.selenium.find_elements_by_css_selector(
            "#main_about #services .card")
        self.assertEqual(len(services), 4)
        # skills
        skills = self.selenium.find_elements_by_css_selector(
            "#main_about #skills .card")
        self.assertEqual(len(skills), 3)
        # services +1
        Term.objects.create(
            category=AboutCategory.objects.get(pk=1),
            logo=os.path.join(BASE_DIR, "uploads/test.png"),
            name_en="test",
            name_fr="test",
            description_en="test",
            description_fr="test",
        )
        self.selenium.get("".join([self.live_server_url, "/about/"]))
        services = self.selenium.find_elements_by_css_selector(
            "#main_about #services .card")
        self.assertEqual(len(services), 5)
        # services -1
        Term.objects.get(name_en="test").delete()
        self.selenium.get("".join([self.live_server_url, "/about/"]))
        services = self.selenium.find_elements_by_css_selector(
            "#main_about #services .card")
        self.assertEqual(len(services), 4)
