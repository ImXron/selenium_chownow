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
    for element in (demo_page.FIELD_ERROR_MESSAGE, demo_page.CLOSE_FIELD_ERROR_MESSAGE_BUTTON):
        assert wait.until(expected_condition.visibility_of_element_located((locate_by.XPATH, element)))

    demo_page.click_error_prompt_close_button()
    for element in (demo_page.FIELD_ERROR_MESSAGE, demo_page.CLOSE_FIELD_ERROR_MESSAGE_BUTTON):
        assert wait.until(expected_condition.invisibility_of_element_located((locate_by.XPATH, element)))


@pytest.mark.ID0006
@pytest.mark.demo_page
def test_fill_out_demo_request_details_and_verify_text_inputs(demo_page,
                                                              wait,
                                                              expected_condition,
                                                              locate_by,
                                                              setup_tear_down):
    first_name = "Bat"
    last_name = "Man"
    restaurant_name = "Everything But Bat"
    zip_code = "uhh...Gotham City's zip code?"
    email = "800-bat-mann"
    phone_number = "800-bat-mann"

    demo_page.go_to()
    assert wait.until(expected_condition.visibility_of_element_located((locate_by.ID, demo_page.FIRST_NAME_FIELD)))

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
