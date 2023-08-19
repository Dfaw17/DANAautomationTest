import time
from selenium.webdriver.common.by import By
from assertpy import assert_that
from mobile.helper.setting import DEVICE_RUN


def elem_wait(sec):
    time.sleep(sec)


def elem_click(open_driver, elem):
    open_driver.find_element(elem.get(DEVICE_RUN)[0], elem.get(DEVICE_RUN)[1]).click()


def input_text(open_driver, elem, text):
    open_driver.find_element(elem.get(DEVICE_RUN)[0], elem.get(DEVICE_RUN)[1]).send_keys(text)


def assert_display(open_driver, elem):
    time.sleep(1)
    open_driver.find_element(elem.get(DEVICE_RUN)[0], elem.get(DEVICE_RUN)[1]).is_displayed()


def assert_text_display(open_driver, text):
    time.sleep(1)
    open_driver.find_element(By.XPATH, f"//*[@text='{text}']").is_displayed()


def assert_text_not_display(open_driver, text):
    time.sleep(1)
    try:
        target = open_driver.find_element(By.XPATH, f"//*[@text='{text}']").is_displayed()
    except:
        target = False
    assert_that(target).is_false()


def assert_not_display(open_driver, elem):
    time.sleep(1)
    try:
        target = open_driver.find_element(elem.get(DEVICE_RUN)[0], elem.get(DEVICE_RUN)[1]).is_displayed()
    except:
        target = False
    assert_that(target).is_false()


def scroll_to_elem(open_driver, elem):
    while True:
        fromx = open_driver.get_window_size().get("width") * 50 / 100
        fromY = open_driver.get_window_size().get("height") * 50 / 100
        tox = open_driver.get_window_size().get("width") * 50 / 100
        toY = open_driver.get_window_size().get("height") * 10 / 100
        open_driver.swipe(fromx, fromY, tox, toY, 400)
        try:
            open_driver.find_element(elem.get(DEVICE_RUN)[0], elem.get(DEVICE_RUN)[1]).is_displayed()
            break
        except:
            pass


def get_lenght(open_driver, elem):
    count = open_driver.find_elements(elem.get(DEVICE_RUN)[0], elem.get(DEVICE_RUN)[1])
    return len(count)


def get_attribute_elem(open_driver, elem, att):
    get_att = open_driver.find_element(elem.get(DEVICE_RUN)[0], elem.get(DEVICE_RUN)[1]).get_attribute(att)
    return get_att