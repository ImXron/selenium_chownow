"""This module models ChowNow's homepage. Oh...were you expecting more? Welp, this is awkward. Jk, I got you!

    The goal here is to abstract away all of the objects on ChowNow's website so we can easily manipulate this page.
    This keeps the actual tests readable AND (wait for it...) maintainable! Meaning, if we have 1000 tests, we don't
    have to refactor all of those tests for when some html element's id changes. Instead, we can open this file and make
    the minor change here in the implementation and boom! --> (Insert "mind blown" meme here).

"""

# TODO: The menu icon also contains buttons that take you to the "how it works", "testimonial" add "pricing" pages.
#       These items are on every page so it looks like they put them in their header/footers of their views, So maybe we
#       can make a class for all the objects on the web page that are always there?

from src.misc.urls import base_url


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        """This method gets us the home page

        :return: None.
        """

        self.driver.get(base_url)

    def click_main_logo(self):
        """This method will click on the ChowNow logo on the top left of the navbar.

        :return: None.
        """

        self.driver.find_element_by_css_selector("div.header__menu .h1_logo a").click()

    def click_how_it_works(self):
        """This method will click on the "how it works" link on the home page.

        :return: None.
        """

        self.driver.find_element_by_link_text("How It Works").click()
