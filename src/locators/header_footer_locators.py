"""This models the header and footer objects that most pages contain. Note: this is not an actual page!

"""

from selenium.webdriver.common.by import By


class HeaderFooterLocators(object):
    """This class contains the Locators for the header and footer objects. These are tuples containing both how to
    locate the element and the actual locator string.

    The first index should use members belonging to Selenium's "By" class.
        Ex: By.ID, By.XPATH, By.CSS, etc.

    The second index is the actual locator string (based off the first index above).

    """

    # Header Links
    LOGO_HEADER = (By.XPATH, "//h1[@class='h1_logo']/a")
    PHONE_NUMBER_HEADER = (By.XPATH, "//a[@class='phone']")
    HOW_IT_WORKS_HEADER = (By.XPATH, "//*[@class='option how']/a")
    TESTIMONIALS_HEADER = (By.XPATH, "//li[@class='option testimonials']/a")
    PRICING_HEADER = (By.XPATH, "//li[@class='option pricing']/a")
    REQUEST_DEMO_HEADER = (By.XPATH, "//li[@class='demo']/a")
    NAV_MENU_HEADER = (By.XPATH, "//p/a[@href='#']")

    # Nav Menu Links
    NAV_MENU = (By.XPATH, "//div[@class='nav__menu']")
    NAV_MENU_CLOSE_BUTTON = (By.XPATH, "//div[@class='nav__menu__close common-close']/a")
    HOW_IT_WORKS_NAV = (By.XPATH, "//ul[@class='main']/li[1]/a")
    TESTIMONIALS_NAV = (By.XPATH, "//ul[@class='main']/li[2]/a")
    PRICING_NAV = (By.XPATH, "//ul[@class='main']/li[3]/a")
    REQUEST_DEMO_NAV = (By.XPATH, "//ul[@class='main']/li[4]/a")
    FLEX_DELIVERY_NAV = (By.XPATH, "//ul[@class='sub']/li[1]/a")
    MARKETING_NAV = (By.XPATH, "//ul[@class='sub']/li[2]/a")
    WEBSITES_NAV = (By.XPATH, "//ul[@class='sub']/li[3]/a")
    ABOUT_US_NAV = (By.XPATH, "//ul[@class='sub']/li[4]/a")
    CAREERS_NAV = (By.XPATH, "//ul[@class='sub']/li[5]/a")
    BLOG_NAV = (By.XPATH, "//ul[@class='sub']/li[6]/a")
    CONTACT_NAV = (By.XPATH, "//ul[@class='sub']/li[6]/a")
    REFUND_POLICY_NAV = (By.XPATH, "//ul[@class='extras']/li[1]/a")
    TERMS_OF_SERVICE_NAV = (By.XPATH, "//ul[@class='extras']/li[2]/a")
    PRIVATE_POLICY_NAV = (By.XPATH, "//ul[@class='extras']/li[3]/a")

    # Footer Links
    LOGO_FOOTER = (By.XPATH, "//div[@class='footer__group left logo']/a")
    HOW_IT_WORKS_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[1]")
    TESTIMONIALS_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[2]")
    PRICING_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[3]")
    BLOG_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[4]")
    MARKETING_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[5]")
    FLEX_DELIVERY_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[6]")
    WEBSITES_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[7]")
    ABOUT_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[8]")
    CAREERS_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[9]")
    CONTACT_US_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[10]")
    REFUND_POLICY_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[11]")
    TERMS_OF_SERVICE_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[12]")
    PRIVATE_POLICY_FOOTER = (By.XPATH, "(//ul[@class='menu']/li/a)[13]")
