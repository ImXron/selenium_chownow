"""This base class will be the parent class of any other page on the website.

"""

from selenium.webdriver.common.by import By


class BasePage(object):
    BASE_URL = "https://www.chownow.com/"

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        """Opens up the URL. When called from a child class, the child's class url will be used instead.

        :return: None
        """
        self.driver.get(self.BASE_URL)

    def get_page_url(self):
        """Gets the URL of the home page. When called from a child class, the child's class url will be used instead.

        :return: (Str) The home page url.
        """
        return self.driver.url

    def get_page_title(self):
        """Gets the title of the home page. When called from a child class, the child's class title will be used instead.

        :return: (Str) The title of the home page.
        """
        return self.driver.title

    def get_element(self, locator):
        """This helper method will return a web element. Be sure to use Selenium's "By" class.

        :param locator: (Tuple): Contains the locator information, use (By.<member>, locator_string)
        :return: Returns a web element
        """
        return self.driver.find_element(*locator)

    @staticmethod
    def click_on(web_element):
        """Generic click method to be used in child classes.

        :param web_element: Web element to be clicked. Use the get_element method above to get the element.
        :return: None.
        """
        web_element.click()

    @staticmethod
    def set_text(web_element, text):
        """Generic set text method to be used in child classes. Use the get_element method above to get the element.

        :param web_element: Web element to set the text on.
        :param text: (Str) The desired text to input into the text field.
        :return: None.
        """
        web_element.clear()
        web_element.send_keys(text)

    def _remove_swipe_element(self):
        """A web element was added to the right side of the pages that have the menu nav button (for touch screen swiping).
        This method will make this element invisible so we can click on the menu nav button (overlaps with this bar).

        :return:
        """
        SWIPE_BAR = (By.CLASS_NAME, "swipe")
        if self.get_element(SWIPE_BAR).is_displayed():
            self.driver.execute_script("document.getElementsByClassName('swipe')[0].style.visibility = 'hidden';")
