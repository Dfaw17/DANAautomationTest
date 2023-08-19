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
    total_data = get_lenght(open_driver, HOME_list_data_todo)
    assert_that(int(total_data)).is_equal_to(3)