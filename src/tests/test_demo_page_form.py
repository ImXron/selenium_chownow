import pytest


@pytest.mark.ID0005
@pytest.mark.demo_page
def test_clicking_request_demo_with_no_text_inputs_filled_out_shows_an_error(demo_page,
                                                                             wait,
                                                                             expected_condition,
                                                                             locate_by,
                                                                             setup_tear_down):
    demo_page.go_to()
    demo_page.click_request_demo_button()
    for element in (demo_page.Locators.FIELD_ERROR_MESSAGE, demo_page.Locators.CLOSE_FIELD_ERROR_MESSAGE_BUTTON):
        assert wait.until(expected_condition.visibility_of_element_located(element))

    demo_page.click_error_prompt_close_button()
    for element in (demo_page.Locators.FIELD_ERROR_MESSAGE, demo_page.Locators.CLOSE_FIELD_ERROR_MESSAGE_BUTTON):
        assert wait.until(expected_condition.invisibility_of_element_located(element))


@pytest.mark.ID0006
@pytest.mark.demo_page
def test_fill_out_demo_request_details_and_verify_text_inputs(demo_page,
                                                              setup_tear_down):
    first_name = "Bat"
    last_name = "Man"
    restaurant_name = "Everything But Bat"
    zip_code = "Uhh...Alfred, please help!"
    email = "Brucey_boy92@wayneenterprises.com"
    phone_number = "800-bma-nnnn"

    demo_page.go_to()
    demo_page.first_name_is(first_name)
    demo_page.last_name_is(last_name)
    demo_page.restaurant_name_is(restaurant_name)
    demo_page.restaurant_zip_code_is(zip_code)
    demo_page.email_is(email)
    demo_page.phone_number_is(phone_number)

    assert demo_page.get_first_name() == first_name
    assert demo_page.get_last_name() == last_name
    assert demo_page.get_restaurant_name() == restaurant_name
    assert demo_page.get_zip_code() == zip_code
    assert demo_page.get_email() == email
    assert demo_page.get_phone_number() == phone_number
