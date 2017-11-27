"""This module models ChowNow's homepage. Oh...were you expecting more? Welp, this is awkward. Jk, I got you!

    The goal here is to abstract away all of the objects on ChowNow's website so we can easily manipulate this page.
    This keeps the actual tests readable AND (wait for it...) maintainable! Meaning, if we have 1000 tests, we don't
    have to refactor all of those tests for when some html element's id changes. Instead, we can open this file and make
    the minor change here in the implementation and boom! --> (Insert "mind blown" meme here).

"""

# TODO: All the Header and footer objects in one class (HeaderFooter...)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(object):
    base_url = "https://www.chownow.com/"

    # Locators
    NAV_MENU_BUTTON = "//div[@class='header__menu']/p/a"
    NAV_MENU_CLOSE_BUTTON = "//div[@class='nav__menu__close common-close']/a"
    NAV_MENU = "//div[@class='nav__menu']"
    MAIN_LOGO = "//h1[@class='h1_logo']/a"
    HOW_IT_WORKS_BUTTON = "//*[@class='option how']/a"
    REQUEST_DEMO_BUTTON = "//li[@class='demo']/a"
    CLOSE_GREEN_NOTIFICATION_BAR = "//*[@class='header__notification__close']/a"

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        """This method gets us the home page

        :return: None.
        """

        self.driver.get(self.base_url)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.CLOSE_GREEN_NOTIFICATION_BAR)))
        self.driver.find_element_by_xpath(self.CLOSE_GREEN_NOTIFICATION_BAR).click()

    def click_main_logo(self):
        """This method will click on the ChowNow logo on the top left of the navbar.

        :return: None.
        """

        self.driver.find_element_by_xpath(self.MAIN_LOGO).click()

    def click_how_it_works_button(self):
        """This method will click on the "how it works" link on the home page.

        :return: None.
        """

        self.driver.find_element_by_xpath(self.HOW_IT_WORKS_BUTTON).click()

    def click_nav_menu_button(self):
        """ This method will click on the menu (hamburger or stack) icon, which opens a context menu.

        :return: None.
        """

        self.driver.find_element_by_xpath(self.NAV_MENU_BUTTON).click()

    def click_nav_menu_close_button(self):
        """ This method will click on the menu close icon (X), which closes the context menu.

        :return: None.
        """

        self.driver.find_element_by_xpath(self.NAV_MENU_CLOSE_BUTTON).click()

    def click_request_demo_button(self):
        """This method will click on the request a demo button the nav bar.

        :return: None.
        """
        self.driver.find_element_by_xpath(self.REQUEST_DEMO_BUTTON).click()
