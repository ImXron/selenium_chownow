"""This module contains the locators for the demo form objects. These locators are the same for ever page that contains
these objects.

"""

from selenium.webdriver.common.by import By


class DemoFormLocators(object):
    """This class contains the Locators for the header and footer objects. These are tuples containing both how to
    locate the element and the actual locator string.

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
