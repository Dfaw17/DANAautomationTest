import pytest
import time
from appium import webdriver
import os


def pytest_html_report_title(report):
    report.title = "Report Mobile Automation"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring


@pytest.fixture()
def open_driver():
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    if worker_id == "gw0":
        my_udid = "emulator-5554"
    elif worker_id == "gw1":
        my_udid = "emulator-5556"
    elif worker_id == "gw2":
        my_udid = "emulator-5558"
    else:
        my_udid = ""
        print("Something went wrong")
    caps = {
        "platformName": "Android",
        "appium:udid": my_udid,
        "appium:appActivity": "com.example.android.architecture.blueprints.todoapp.tasks.TasksActivity",
        "appium:appPackage": "com.example.android.architecture.blueprints.todomvp.mock",
        "autoGrantPermissions": True,
        "appium:noReset": False,
    }
    driver = webdriver.Remote(f"http://127.0.0.1:4723/wd/hub", desired_capabilities=caps)
    return driver


@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    # print("before test")
    open_driver.implicitly_wait(2)
    yield
    # print("after test")
    print("Test Success")
    open_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # print("\nbefore suite")
    yield
    # print("after suite")
