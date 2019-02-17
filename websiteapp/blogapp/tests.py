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
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual("Blog", header_title.text)
        links = self.selenium.find_elements_by_css_selector(
            "#header_blog li a")
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0].text, "Catégorie 1")
        self.assertEqual(links[1].text, "Catégorie 2")
        # main
        categories = self.selenium.find_elements_by_css_selector(
            "#main_blog .container")
        self.assertEqual(len(categories), 2)

        def assert_post_in_category(category, number_cards):
            posts = category.find_elements_by_class_name(
                "card")
            self.assertEqual(len(posts), number_cards)
        # Category 1
        assert_post_in_category(categories[0], 1)
        # Category 2
        assert_post_in_category(categories[1], 2)
        # Link to post
        links = categories[1].find_elements_by_tag_name("a")
        links[0].click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "header_post")))
        self.assertEqual(
            "http://localhost:12345/blog/3/", self.selenium.current_url)

    def test_post(self):
        """ tests for post page"""
        self.selenium.get("".join([self.live_server_url, "/blog/1/"]))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual("Catégorie 1", header_title.text)
        project_title = self.selenium.find_element_by_tag_name("h2")
        self.assertEqual("Article 1", project_title.text)
        # main
        card_bodies = self.selenium.find_elements_by_css_selector(
            "#main_post .card .card-body")
        self.assertEqual(len(card_bodies), 2)
        # comments
        comment_titles = card_bodies[1].find_elements_by_tag_name("h5")
        self.assertEqual(comment_titles[0].text, "Commentaires")
        self.assertEqual(comment_titles[1].text, "Laisser un commentaire")
        comments = card_bodies[1].find_elements_by_class_name("row")
        self.assertEqual(len(comments), 4)
        # comment form
        form = card_bodies[1].find_element_by_tag_name("form")
        form.find_element_by_id("id_author_name").send_keys("test 6")
        form.find_element_by_id("id_author_email").send_keys("test6@test.com")
        form.find_element_by_id("id_text").send_keys("cool !")
        form.find_element_by_tag_name("button").click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert")))
        message = self.selenium.find_element_by_css_selector(
            "#header_post .container div")
        self.assertEqual(
            message.text,
            "Votre commentaire sera ajouté après validation de ma part.")
        # valid the comment
        comment = Comment.objects.get(author_name="test 6")
        comment.valid = True
        comment.save()
        self.selenium.get("".join([self.live_server_url, "/blog/1/"]))
        card_bodies = self.selenium.find_elements_by_css_selector(
            "#main_post .card .card-body")
        comments = card_bodies[1].find_elements_by_class_name("row")
        self.assertEqual(len(comments), 5)
