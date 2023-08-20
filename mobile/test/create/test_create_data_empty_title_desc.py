import time
from mobile.helper.actions import *
from mobile.pom.POM_home_page import *
from mobile.pom.POM_create_page import *


def test(open_driver):

    # TEST
    elem_click(open_driver, HOME_btn_add)
    input_text(open_driver, CREATE_if_title, "")
    input_text(open_driver, CREATE_if_desc, "")
    elem_click(open_driver, CREATE_btn_submit)
    assert_display(open_driver, CREATE_page)
