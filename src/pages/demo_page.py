"""This module models ChowNow's demo page.

"""


# TODO: There are places where we are finding elements multiple times. Need to refactor so we only do this once!

class DemoPage(object):
    base_url = "https://www.chownow.com/demo"

    # Locators. There is no need to make these instance variables, as they are constant. Uppercase per pep8 ;)
    FIRST_NAME_FIELD = "FirstName"
    LAST_NAME_FIELD = "LastName"
    RESTAURANT_NAME_FIELD = "Company"
    RESTAURANT_ZIP_CODE_FIELD = "PostalCode"
    EMAIL_FIELD = "//input[@id='Email']"
    PHONE_NUMBER_FIELD = "//input[@id='Phone']"
    REQUEST_DEMO_BUTTON = "//span//button[@type='submit']"
    FIELD_ERROR_MESSAGE = "//p[contains(text(), 'Oops.')]"
    CLOSE_FIELD_ERROR_MESSAGE_BUTTON = "//div[@class='error__close common-close']/a"
    WHY_ARE_YOU_MOST_INTERESTED_COMBO_BOX = "//select[@id='Why_Interested_in_Online_Ordering__c']"

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        """This method gets us the demo page

        :return: None.
        """

        self.driver.get(self.base_url)

    def first_name_is(self, first_name):
        """Enters in a name for the first name field.

        :param first_name: (Str) Name that is desired to be entered in the first name field.
        :return: None.
        """
        self.driver.find_element_by_id(self.FIRST_NAME_FIELD).clear()
        self.driver.find_element_by_id(self.FIRST_NAME_FIELD).send_keys(first_name)

    def last_name_is(self, last_name):
        """Enters in a name for the last name field.

        :param last_name: (Str) Name that is desired to be entered in the last name field.
        :return: None.
        """
        self.driver.find_element_by_id(self.LAST_NAME_FIELD).clear()
        self.driver.find_element_by_id(self.LAST_NAME_FIELD).send_keys(last_name)

    def restaurant_name_is(self, restaurant_name):
        """Enters in a name for the restaurant name field.

        :param restaurant_name: (Str) Name that is desired to be entered in the restaurant name field.
        :return: None.
        """
        self.driver.find_element_by_id(self.RESTAURANT_NAME_FIELD).clear()
        self.driver.find_element_by_id(self.RESTAURANT_NAME_FIELD).send_keys(restaurant_name)

    def restaurant_zip_code_is(self, restaurant_zip_code):
        """Enters in a number for the restaurant zip code field.

        :param restaurant_zip_code: (Str) Name that is desired to be entered in the restaurant zip code field.
        :return: None.
        """
        self.driver.find_element_by_id(self.RESTAURANT_ZIP_CODE_FIELD).clear()
        self.driver.find_element_by_id(self.RESTAURANT_ZIP_CODE_FIELD).send_keys(restaurant_zip_code)

    def email_is(self, email):
        """Enters in an email address for the email field.

        :param email: (Str) Email address that is desired to be entered in the email field.
        :return: None.
        """
        self.driver.find_element_by_xpath(self.EMAIL_FIELD).clear()
        self.driver.find_element_by_xpath(self.EMAIL_FIELD).send_keys(email)

    def phone_number_is(self, phone_number):
        """Enters in a number for the phone number field.

        :param phone_number: (Str) Phone number without any "-".
        :return: None.
        """
        self.driver.find_element_by_xpath(self.PHONE_NUMBER_FIELD).clear()
        self.driver.find_element_by_xpath(self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def click_request_demo_button(self):
        """Clicks on the request a demo button. DON"T USE THIS IF YOU ACTUALLY FILL OUT THE FORM!!!

        :return: None.
        """
        self.driver.find_element_by_xpath(self.REQUEST_DEMO_BUTTON).click()

    def click_error_prompt_close_button(self):
        """Clicks on the close "X" button when an error message pops up from invalid text input.

        :return: None.
        """
        self.driver.find_element_by_xpath(self.CLOSE_FIELD_ERROR_MESSAGE_BUTTON).click()

    # ==================================================================================================================
    # Getters
    # ==================================================================================================================
    _attribute = "value"

    def get_first_name(self):
        """Gets the value in the first name text input

        :return: (Str) Returns the text in the first name field.
        """
        return self.driver.find_element_by_id(self.FIRST_NAME_FIELD).get_attribute(self._attribute)

    def get_last_name(self):
        """Gets the value in the last name text input

        :return: (Str) Returns the text in the last name field.
        """
        return self.driver.find_element_by_id(self.LAST_NAME_FIELD).get_attribute(self._attribute)

    def get_restaurant_name(self):
        """Gets the value in the restaurant name text input

        :return: (Str) Returns the text in the restaurant name field.
        """
        return self.driver.find_element_by_id(self.RESTAURANT_NAME_FIELD).get_attribute(self._attribute)

    def get_zip_code(self):
        """Gets the value in the zip code text input

        :return: (Str) Returns the text in the zip code field.
        """
        return self.driver.find_element_by_id(self.RESTAURANT_ZIP_CODE_FIELD).get_attribute(self._attribute)

    def get_email(self):
        """Gets the value in the email text input

        :return: (Str) Returns the text in the email field.
        """
        return self.driver.find_element_by_xpath(self.EMAIL_FIELD).get_attribute(self._attribute)

    def get_phone_number(self):
        """Gets the value in the phone number text input

        :return: (Str) Returns the text in the phone number field.
        """
        return self.driver.find_element_by_xpath(self.PHONE_NUMBER_FIELD).get_attribute(self._attribute)
