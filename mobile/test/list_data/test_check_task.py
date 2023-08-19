import time
from mobile.helper.actions import *
from mobile.pom.POM_home_page import *
from mobile.pom.POM_create_page import *
from mobile.pom.POM_detail_page import *
from mobile.helper.shared_step import *


def test(open_driver):
    # TEST
    STEP_ADD_DATA(open_driver)
    STEP_ADD_DATA(open_driver)
    STEP_ADD_DATA(open_driver)
    elem_click(open_driver, HOME_checked_1)
    elem_click(open_driver, HOME_checked_2)
    assert_that(get_attribute_elem(open_driver, HOME_checked_1, "checked")).is_equal_to("true")
    assert_that(get_attribute_elem(open_driver, HOME_checked_2, "checked")).is_equal_to("true")