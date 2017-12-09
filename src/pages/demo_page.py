"""This module models ChowNow's demo page.

"""

from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DemoPage(BasePage):
    BASE_URL = "https://www.chownow.com/demo"
    PAGE_TITLE = "Free Demo - Try Restaurant Software and Apps from ChowNow"

    class Locators(object):
        """This class contains the Locators for the demo page. These are tuples containing both how to locate the element
        and the actual locator string.

        The first index should use members belonging to Selenium's "By" class.
            Ex: By.ID, By.XPATH, By.CSS, etc.

        The second index is the actual locator string (based off the first index above).

        """
        FIRST_NAME_FIELD = (By.ID, "FirstName")
        LAST_NAME_FIELD = (By.ID, "LastName")
        RESTAURANT_NAME_FIELD = (By.ID, "Company")
        RESTAURANT_ZIP_CODE_FIELD = (By.ID, "PostalCode")
        EMAIL_FIELD = (By.XPATH, "//input[@id='Email']")
        PHONE_NUMBER_FIELD = (By.XPATH, "//input[@id='Phone']")
        REQUEST_DEMO_BUTTON = (By.XPATH, "//span//button[@type='submit']")
        FIELD_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Oops.')]")
        CLOSE_FIELD_ERROR_MESSAGE_BUTTON = (By.XPATH, "//div[@class='error__close common-close']/a")
        WHY_ARE_YOU_MOST_INTERESTED_COMBO_BOX = (By.XPATH, "//select[@id='Why_Interested_in_Online_Ordering__c']")

    def go_to(self):
        """This method gets us the demo page

        :return: None.
        """
        super(DemoPage, self).go_to(self.get_page_url())

    # ==================================================================================================================
    # Clicks
    # ==================================================================================================================

    def click_request_demo_button(self):
        """Clicks on the request a demo button. DON"T USE THIS IF YOU ACTUALLY FILL OUT THE FORM!!!

        :return: None.
        """
        self.click_on(self.get_element(self.Locators.REQUEST_DEMO_BUTTON))

    def click_error_prompt_close_button(self):
        """Clicks on the close "X" button when an error message pops up from invalid text input.

        :return: None.
        """
        self.click_on(self.get_element(self.Locators.CLOSE_FIELD_ERROR_MESSAGE_BUTTON))

    # ==================================================================================================================
    # Setters
    # ==================================================================================================================

    def first_name_is(self, first_name):
        """Enters in a name for the first name field.

        :param first_name: (Str) Name that is desired to be entered in the first name field.
        :return: None.
        """
        self.set_text(self.get_element(self.Locators.FIRST_NAME_FIELD), first_name)
        assert self.get_first_name() == first_name

    def last_name_is(self, last_name):
        """Enters in a name for the last name field.

        :param last_name: (Str) Name that is desired to be entered in the last name field.
        :return: None.
        """
        self.set_text(self.get_element(self.Locators.LAST_NAME_FIELD), last_name)
        assert self.get_last_name() == last_name

    def restaurant_name_is(self, restaurant_name):
        """Enters in a name for the restaurant name field.

        :param restaurant_name: (Str) Name that is desired to be entered in the restaurant name field.
        :return: None.
        """
        self.set_text(self.get_element(self.Locators.RESTAURANT_NAME_FIELD), restaurant_name)
        assert self.get_restaurant_name() == restaurant_name

    def restaurant_zip_code_is(self, restaurant_zip_code):
        """Enters in a number for the restaurant zip code field.

        :param restaurant_zip_code: (Str) Name that is desired to be entered in the restaurant zip code field.
        :return: None.
        """
        self.set_text(self.get_element(self.Locators.RESTAURANT_ZIP_CODE_FIELD), restaurant_zip_code)
        assert self.get_zip_code() == restaurant_zip_code

    def email_is(self, email):
        """Enters in an email address for the email field.

        :param email: (Str) Email address that is desired to be entered in the email field.
        :return: None.
        """
        self.set_text(self.get_element(self.Locators.EMAIL_FIELD), email)
        assert self.get_email() == email

    def phone_number_is(self, phone_number):
        """Enters in a number for the phone number field.

        :param phone_number: (Str) Phone number without any "-".
        :return: None.
        """
        self.set_text(self.get_element(self.Locators.PHONE_NUMBER_FIELD), phone_number)
        assert self.get_phone_number() == phone_number

    # ==================================================================================================================
    # Getters
    # ==================================================================================================================

    _attribute = "value"

    # TODO: Dry up this wet code please

    def get_first_name(self):
        """Gets the value in the first name text input

        :return: (Str) Returns the text in the first name field.
        """
        return self.get_element(self.Locators.FIRST_NAME_FIELD).get_attribute(self._attribute)

    def get_last_name(self):
        """Gets the value in the last name text input

        :return: (Str) Returns the text in the last name field.
        """
        return self.get_element(self.Locators.LAST_NAME_FIELD).get_attribute(self._attribute)

    def get_restaurant_name(self):
        """Gets the value in the restaurant name text input

        :return: (Str) Returns the text in the restaurant name field.
        """
        return self.get_element(self.Locators.RESTAURANT_NAME_FIELD).get_attribute(self._attribute)

    def get_zip_code(self):
        """Gets the value in the zip code text input

        :return: (Str) Returns the text in the zip code field.
        """
        return self.get_element(self.Locators.RESTAURANT_ZIP_CODE_FIELD).get_attribute(self._attribute)

    def get_email(self):
        """Gets the value in the email text input

        :return: (Str) Returns the text in the email field.
        """
        return self.get_element(self.Locators.EMAIL_FIELD).get_attribute(self._attribute)

    def get_phone_number(self):
        """Gets the value in the phone number text input

        :return: (Str) Returns the text in the phone number field.
        """
        return self.get_element(self.Locators.PHONE_NUMBER_FIELD).get_attribute(self._attribute)
