import time
from mobile.helper.actions import *
from mobile.pom.POM_home_page import *
from mobile.pom.POM_create_page import *
from mobile.pom.POM_detail_page import *
from mobile.helper.shared_step import *


def test(open_driver):
    # DATA
    text_title = f"Task {int(time.time() * 1000)} EDIT"

    # TEST
    STEP_ADD_DATA(open_driver)
    elem_click(open_driver, HOME_data_1)
    elem_click(open_driver, DETAIL_btn_edit)
    input_text(open_driver, CREATE_if_title, text_title)
    input_text(open_driver, CREATE_if_desc, "Test Feature Deposit With BCA EDIT")
    elem_click(open_driver, CREATE_btn_submit)
    assert_text_display(open_driver, text_title)
