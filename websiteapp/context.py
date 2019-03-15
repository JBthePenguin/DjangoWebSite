from websitedjango import settings
from websiteapp.models import (
    get_navbar_items, get_footer_items, get_social_links)


class Context(dict):
    """Default Context"""
    def __init__(self):
        """ settings for site's theme,
        language , navbar and footer """
        super(Context, self).__init__()
        # Theme
        # class for background, navbar and button
        bg_class = "bg-{}".format(settings.THEME)
        navbar_class = "navbar-{}".format(settings.THEME)
        btn_class = "btn-{}".format(settings.THEME)
        # theme and langage button
        if settings.THEME == "dark":
            btn_theme = "checked"
            btn_lang_style = "light"
        else:
            btn_theme = "unchecked"
            btn_lang_style = "dark"
        # Langage
        # button
        if settings.LANGUAGE_CODE == "fr":
            btn_lang = "checked"
        else:
            btn_lang = "unchecked"
        # Navbar items
        navbar_items = get_navbar_items()
        # Footer
        # items
        footer_items = get_footer_items()
        # social links
        social_links = get_social_links()
        self.update(
            bg_class=bg_class, navbar_class=navbar_class,
            btn_class=btn_class, btn_theme=btn_theme,
            btn_lang_style=btn_lang_style, lang=settings.LANGUAGE_CODE,
            btn_lang=btn_lang, navbar_items=navbar_items,
            footer_items=footer_items, social_links=social_links)
