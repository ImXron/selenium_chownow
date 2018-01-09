"""This module models ChowNow's homepage. Oh...were you expecting more? Welp, this is awkward. Jk, I got you!

    The goal here is to abstract away all of the objects on ChowNow's website so we can easily manipulate this page.
    This keeps the actual tests readable AND (wait for it...) maintainable! Meaning, if we have 1000 tests, we don't
    have to refactor all of those tests for when some html element's id changes. Instead, we can open this file and make
    the minor change here in the implementation and boom! --> (Insert "mind blown" meme here).

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.locators.demo_form_locators import DemoFormLocators
from src.locators.header_footer_locators import HeaderFooterLocators
from src.pages.base_page import BasePage


class HomePage(BasePage):
    BASE_URL = "https://www.chownow.com/"
    PAGE_TITLE = "Online Food Ordering System & App - ChowNow"
    TIMEOUT = 5

    class Locators(HeaderFooterLocators, DemoFormLocators):
        """This class contains the Locators for the home page. These are tuples containing both how to locate the element
        and the actual locator string.

        The first index should use members belonging to Selenium's "By" class.
            Ex: By.ID, By.XPATH, By.CSS, etc.

        The second index is the actual locator string (based off the first index above).

        """
        CLOSE_GREEN_NOTIFICATION_BAR = (By.XPATH, "//*[@class='header__notification__close']/a")
        WATCH_VIDEO_BUTTON = (By.CSS_SELECTOR, ".common-button.standard.watch.js")
        VIDEO_FRAME = (By.NAME, "wistia_embed")
        VIDEO_CLOSE_BUTTON = (By.XPATH, "//div[@class='modal__close common-close']/a")

    def go_to(self):
        """This method gets us to the home page.

        :return: None.
        """

        self.driver.get(self.BASE_URL)
        self.close_header_notification()
        self._remove_swipe_element()

    def click_main_logo(self):
        """This method will click on the ChowNow logo on the top left of the nav bar.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.LOGO_HEADER))

    def click_how_it_works_button(self):
        """This method will click on the "how it works" link on the home page.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.HOW_IT_WORKS_HEADER))

    def click_nav_menu_button(self):
        """ This method will click on the menu (hamburger or stack) icon, which opens a context menu.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.NAV_MENU_HEADER))

    def click_nav_menu_close_button(self):
        """ This method will click on the menu close icon (X), which closes the context menu.

        :return: None.
        """

        self.click_on(self.get_element(self.Locators.NAV_MENU_CLOSE_BUTTON))

    def click_request_demo_button(self):
        """This method will click on the request a demo button the nav bar.

        :return: None.
        """
        self.click_on(self.get_element(self.Locators.REQUEST_DEMO_HEADER))

    def click_watch_video_button(self):
        """This method will click on the watch video button.

        :return: None.
        """
        self.click_on(self.get_element(self.Locators.WATCH_VIDEO_BUTTON))

    def click_close_video_button(self):
        """This method will click the x button to close the video pop up.

        :return: None.
        """
        if self.get_element(self.Locators.VIDEO_CLOSE_BUTTON).is_displayed():
            self.click_on(self.get_element(self.Locators.VIDEO_CLOSE_BUTTON))

    def close_header_notification(self):
        """This method closes the green notification bar that pops up when visiting the home page.

        This bar will causes issues when trying to click on elements on the home page.
        NOTE: This should get called when visiting the home page (even from another page).

        :return: None.
        """
        wait = WebDriverWait(self.driver, self.TIMEOUT)
        wait.until(expected_conditions.visibility_of_element_located(self.Locators.CLOSE_GREEN_NOTIFICATION_BAR))

        if self.get_element(self.Locators.CLOSE_GREEN_NOTIFICATION_BAR).is_displayed():
            self.click_on(self.get_element(self.Locators.CLOSE_GREEN_NOTIFICATION_BAR))
