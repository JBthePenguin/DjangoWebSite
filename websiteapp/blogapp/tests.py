from websiteapp.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from websiteapp.blogapp.models import Comment


class BrowseBlogTests(Browser):
    """ Tests for blog.html and post.html"""

    def test_blog(self):
        """ tests for blog page"""
        self.selenium.get("".join([self.live_server_url, "/blog/"]))
        # title
        self.assertEqual(self.selenium.title, "Django Website|Blog")
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual("Blog", header_title.text)
        links = self.selenium.find_elements_by_css_selector(
            "#header_blog li a")
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0].text, "Front-End")
        self.assertEqual(links[1].text, "Back-End")
        # main
        categories = self.selenium.find_elements_by_css_selector(
            "#main_blog .container")
        self.assertEqual(len(categories), 2)

        def assert_post_in_category(category, number_cards):
            posts = category.find_elements_by_class_name(
                "card")
            self.assertEqual(len(posts), number_cards)
        # Category 1
        assert_post_in_category(categories[0], 2)
        # Category 2
        assert_post_in_category(categories[1], 1)
        # Link to post
        links = categories[1].find_elements_by_tag_name("a")
        links[0].click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "button")))
        self.assertEqual(
            "http://localhost:12345/blog/django/", self.selenium.current_url)

    def test_post(self):
        """ tests for post page"""
        self.selenium.get("".join([self.live_server_url, "/blog/jquery/"]))
        # title
        self.assertEqual(
            self.selenium.title, "Django Website|Blog|Front-End")
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual("Blog|Front-End", header_title.text)
        project_title = self.selenium.find_element_by_tag_name("h3")
        self.assertEqual("jQuery", project_title.text)
        # main
        card_bodies = self.selenium.find_elements_by_css_selector(
            "#main_blog .card .card-body")
        self.assertEqual(len(card_bodies), 2)
        # comments
        comment_titles = card_bodies[1].find_elements_by_tag_name("h5")
        self.assertEqual(comment_titles[0].text, "Commentaires")
        self.assertEqual(comment_titles[1].text, "Laisser un commentaire")
        comments = card_bodies[1].find_elements_by_class_name("comment-saved")
        self.assertEqual(len(comments), 1)
        # comment form
        form = card_bodies[1].find_element_by_tag_name("form")
        form.find_element_by_id("id_author_name").send_keys("test 6")
        form.find_element_by_id("id_author_email").send_keys("test6@test.com")
        form.find_element_by_id("id_text").send_keys("cool !")
        form.find_element_by_tag_name("button").click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert")))
        message = self.selenium.find_element_by_css_selector(
            "#main_blog .card .card-body .alert")
        self.assertEqual(
            message.text,
            "Votre commentaire sera ajouté dès que je l'aurai validé.")
        # valid the comment
        comment = Comment.objects.get(author_name="test 6")
        comment.valid = True
        comment.save()
        self.selenium.get("".join([self.live_server_url, "/blog/jquery/"]))
        card_bodies = self.selenium.find_elements_by_css_selector(
            "#main_blog .card .card-body")
        comments = card_bodies[1].find_elements_by_class_name("comment-saved")
        self.assertEqual(len(comments), 2)
