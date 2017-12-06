"""This base class will be the parent class of any other page on the website.

"""


class BasePage(object):
    BASE_URL = "https://www.chownow.com/"
    PAGE_TITLE = ""

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        """Opens up the URL. When called from a child class, the child's class url will be used instead.

        :param url: (Str) The desired URL to open.
        :return: None
        """
        self.driver.get(self.get_page_url())

    def get_page_url(self):
        """Gets the URL of the home page. When called from a child class, the child's class url will be used instead.

        :return: (Str) The home page url.
        """
        return self.BASE_URL

    def get_page_title(self):
        """Gets the title of the home page. When called from a child class, the child's class title will be used instead.

        :return: (Str) The title of the home page.
        """
        return self.PAGE_TITLE

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
