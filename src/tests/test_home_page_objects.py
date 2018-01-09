import pytest


# One super cool thing about the pytest framework is that we can "mark" each test and run tests based on the marks we
# specify. A practical example would be if we are looking at a test case within a test case manager. We can read through
# The test procedure and simple use the pytest command to pass the ID to run the test case!
# Another mark here specified here is "home_page". If someone wanted to only run the tests associated to the
# "home_page", all the tests  marked with "home_page" will run! You can also ignore tests like this...neat-o!


@pytest.mark.ID0001
@pytest.mark.home_page
def test_clicking_the_chownow_logo_from_the_homepage_will_take_us_to_the_homepage(home_page,
                                                                                  expected_condition,
                                                                                  setup_tear_down):
    home_page.go_to()
    home_page.click_main_logo()
    assert expected_condition.title_is("Online Food Ordering System & App - ChowNow")


@pytest.mark.ID0002
@pytest.mark.home_page
def test_clicking_the_how_it_works_link_from_the_homepage_takes_us_to_the_how_it_works_page(home_page,
                                                                                            expected_condition,
                                                                                            setup_tear_down):
    home_page.go_to()
    home_page.click_how_it_works_button()
    assert expected_condition.title_is("Restaurant Mobile App & Online Ordering System - ChowNow")


@pytest.mark.ID0003
@pytest.mark.home_page
def test_can_open_nav_menu_with_button_and_close_with_close_button(home_page,
                                                                   wait,
                                                                   expected_condition,
                                                                   setup_tear_down):
    home_page.go_to()
    home_page.click_nav_menu_button()
    for element in (home_page.Locators.NAV_MENU_CLOSE_BUTTON, home_page.Locators.NAV_MENU):
        assert wait.until(expected_condition.visibility_of_element_located(element))

    home_page.click_nav_menu_close_button()
    for element in (home_page.Locators.NAV_MENU_CLOSE_BUTTON, home_page.Locators.NAV_MENU):
        assert wait.until(expected_condition.invisibility_of_element_located(element))


@pytest.mark.ID0004
@pytest.mark.home_page
def test_clicking_the_request_demo_button_from_the_homepage_navbar_will_take_us_to_the_demo_page(home_page,
                                                                                                 expected_condition,
                                                                                                 setup_tear_down):
    home_page.go_to()
    home_page.click_request_demo_button()
    assert expected_condition.title_is("Free Demo - Try Restaurant Software and Apps from ChowNow")


@pytest.mark.ID0008
@pytest.mark.home_page
def test_clicking_on_watch_video_starts_the_video_and_close_button_closes_it(home_page,
                                                                             expected_condition,
                                                                             wait,
                                                                             setup_tear_down):
    home_page.go_to()
    home_page.click_watch_video_button()
    for element in (home_page.Locators.VIDEO_FRAME, home_page.Locators.VIDEO_CLOSE_BUTTON):
        assert wait.until(expected_condition.visibility_of_element_located(element))

    home_page.click_close_video_button()
    for element in (home_page.Locators.VIDEO_FRAME, home_page.Locators.VIDEO_CLOSE_BUTTON):
        assert wait.until(expected_condition.invisibility_of_element_located(element))
