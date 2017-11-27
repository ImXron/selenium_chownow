"""This conftest file applies to all of the test files in this directory.

    The goal is to create test fixtures that produce and return dependencies. Using dependency injection, we can simply
    "inject" dependencies into our test when needed. This way, we should never have to instantiate objects inside of
    our tests. This is awesome because it keeps tests cleaner and high level for the non-programmers :)

"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from src.pages.demo_page import DemoPage
from src.pages.home_page import HomePage


@pytest.fixture
def chrome_driver():
    """This fixture creates a new instance of the chrome driver. The benefit here is that we NEVER have to create a
       driver from scratch! We simply just pass this fixture into anything that needs it.

    :return: Chrome web driver object.
    """

    return webdriver.Chrome()


@pytest.fixture
def setup_tear_down(chrome_driver):
    """This fixture will run at the beginning and end of each test.

    :param chrome_driver: Chrome web driver instance.
    :return: None.
    """
    chrome_driver.maximize_window()
    yield
    chrome_driver.quit()


@pytest.fixture
def home_page(chrome_driver):
    """This fixture creates an instance of the home page object.

    :return: Returns a new instance of the home page.
    """

    return HomePage(chrome_driver)


@pytest.fixture
def demo_page(chrome_driver):
    """This fixture creates an instance of the demo page object.

    :return: Returns a new instance of the demo page.
    """

    return DemoPage(chrome_driver)


@pytest.fixture
def wait(chrome_driver):
    """This fixture simply returns an instance of the wait class.

    :return: Returns a wait instance.
    """

    wait_time = 15
    return WebDriverWait(chrome_driver, wait_time)


@pytest.fixture
def expected_condition():
    """This fixture simply returns the expected conditions module. The 's' was removed to avoid conflicts and it
    actually reads better --> expected_condition.title_contains("Omg cats are the best animals ever!")

    :return: The expected_conditions module, which contains classes for many different conditions.
    """

    return expected_conditions


@pytest.fixture
def locate_by():
    """

    :return: The by module, which contains supported locator strategies.
    """

    return By
