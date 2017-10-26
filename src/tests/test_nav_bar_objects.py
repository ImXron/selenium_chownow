import pytest


# One super cool thing about the pytest framework is that we can "mark" each test and run tests based on the marks we
# specify. A practical example would be if we are looking at a test case within a test case manager. We can read through
# The test procedure and simple use the pytest command to pass the ID to run the test case!
# Another mark here specified here is "home_page". If someone wanted to only run the tests associated to the
# "home_page", all the tests  marked with "home_page" will run! You can also ignore tests like this...neat-o!

@pytest.mark.ID0001
@pytest.mark.homepage
def test_clicking_the_chownow_logo_from_the_homepage_will_take_us_to_the_homepage(home_page,
                                                                                  wait,
                                                                                  expected_condition,
                                                                                  tear_down):
    home_page.go_to()
    home_page.click_main_logo()

    assert wait.until(expected_condition.title_is("Online Food Ordering System & App - ChowNow"),
                      "Invalid Title!")


@pytest.mark.ID0002
@pytest.mark.homepage
def test_clicking_the_how_it_works_link_from_the_homepage_takes_us_to_the_how_it_works_page(home_page,
                                                                                            wait,
                                                                                            expected_condition,
                                                                                            tear_down):
    home_page.go_to()
    home_page.click_how_it_works()

    assert wait.until(expected_condition.title_is("Restaurant Mobile App & Online Ordering System - ChowNow"),
                      "Invalid Title!")
