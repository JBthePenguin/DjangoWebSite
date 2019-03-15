from websiteapp.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from websiteapp.contactapp.models import Message


class BrowseContactTests(Browser):
    """ Tests for contact.html"""
    def test_contact(self):
        """ tests for contact page"""
        self.selenium.get("".join([self.live_server_url, "/contact/"]))
        # title
        self.assertEqual(self.selenium.title, "Django Website | Contact")
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        subtitle = self.selenium.find_element_by_css_selector("h3 p")
        self.assertEqual("Contact", header_title.text)
        self.assertEqual("Contactez-moi", subtitle.text)
        contact_items = self.selenium.find_elements_by_css_selector(
            "#main_contact li")
        self.assertEqual(len(contact_items), 3)
        # main
        main_title = self.selenium.find_element_by_tag_name("h5")
        self.assertEqual(main_title.text, "Formulaire de contact")
        # contact form
        form = self.selenium.find_element_by_tag_name("form")
        form.find_element_by_id("id_contact_name").send_keys("test 6")
        form.find_element_by_id("id_contact_email").send_keys("test6@test.com")
        form.find_element_by_id("id_subject").send_keys("subject 1")
        form.find_element_by_id("id_content").send_keys("coucou")
        form.find_element_by_tag_name("button").click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert")))
        message = self.selenium.find_element_by_css_selector(
            "#main_contact .alert")
        self.assertEqual(message.text, "Votre message a été envoyé.")
        message = Message.objects.get(contact_name="test 6")
        self.assertEqual(message.subject, "subject 1")
