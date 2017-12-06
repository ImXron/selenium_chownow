"""This module models ChowNow's homepage. Oh...were you expecting more? Welp, this is awkward. Jk, I got you!

    The goal here is to abstract away all of the objects on ChowNow's website so we can easily manipulate this page.
    This keeps the actual tests readable AND (wait for it...) maintainable! Meaning, if we have 1000 tests, we don't
    have to refactor all of those tests for when some html element's id changes. Instead, we can open this file and make
    the minor change here in the implementation and boom! --> (Insert "mind blown" meme here).

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.base_page import BasePage


class HomePage(BasePage):
    BASE_URL = "https://www.chownow.com/"
    PAGE_TITLE = "Online Food Ordering System & App - ChowNow"

    class Locators(object):
        """This class contains the Locators for the home page. These are tuples containing both how to locate the element
        and the actual locator string.

        The first index should use members belonging to Selenium's "By" class.
            Ex: By.ID, By.XPATH, By.CSS, etc.

        The second index is the actual locator string (based off the first index above).

        """
        NAV_MENU_BUTTON = (By.XPATH, "//div[@class='header__menu']/p/a")
        NAV_MENU_CLOSE_BUTTON = (By.XPATH, "//div[@class='nav__menu__close common-close']/a")
        NAV_MENU = (By.XPATH, "//div[@class='nav__menu']")
        MAIN_LOGO = (By.XPATH, "//h1[@class='h1_logo']/a")
        HOW_IT_WORKS_BUTTON = (By.XPATH, "//*[@class='option how']/a")
        REQUEST_DEMO_BUTTON = (By.XPATH, "//li[@class='demo']/a")
        CLOSE_GREEN_NOTIFICATION_BAR = (By.XPATH, "//*[@class='header__notification__close']/a")

    # TODO: This assumes that we will visit the home page once during a test. If the green bar is not there, error!
    def go_to(self):
        """This method gets us to the home page.

        NOTE: There is a green drop down message when visiting the home page for the first time. This will interfere
        with our tests, so this method will find it and close it before proceeding.

        :return: None.
        """

        super(HomePage, self).go_to(self.get_page_url())
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(self.Locators.CLOSE_GREEN_NOTIFICATION_BAR))
        self.click_on(self.get_element(self.Locators.CLOSE_GREEN_NOTIFICATION_BAR))

    def click_main_logo(self):
        """This method will click on the ChowNow logo on the top left of the nav bar.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.MAIN_LOGO))

    def click_how_it_works_button(self):
        """This method will click on the "how it works" link on the home page.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.HOW_IT_WORKS_BUTTON))

    def click_nav_menu_button(self):
        """ This method will click on the menu (hamburger or stack) icon, which opens a context menu.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.NAV_MENU_BUTTON))

    def click_nav_menu_close_button(self):
        """ This method will click on the menu close icon (X), which closes the context menu.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.NAV_MENU_CLOSE_BUTTON))

    def click_request_demo_button(self):
        """This method will click on the request a demo button the nav bar.

        :return: None.
        """
        self.click_on(self.get_element(self.Locators.REQUEST_DEMO_BUTTON))
