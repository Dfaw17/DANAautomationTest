import time
from mobile.helper.actions import *
from mobile.pom.POM_home_page import *
from mobile.pom.POM_create_page import *
from mobile.pom.POM_detail_page import *
from mobile.helper.shared_step import *


def test(open_driver):
    # TEST
    STEP_ADD_DATA(open_driver)
    elem_click(open_driver, HOME_data_1)
    elem_click(open_driver, DETAIL_btn_delete)
    assert_display(open_driver, HOME_no_task)
