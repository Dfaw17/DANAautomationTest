import json
import pytest


def pytest_html_report_title(report):
    report.title = "Report Http Automation"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    # BEFORE TEST
    get_error = request.session.testsfailed

    yield
    # AFTER TEST
    test_result = request.session.testsfailed - get_error

    if test_result == 0:
        with open('data.json', 'r') as file:
            data = json.load(file)
        data['success'].append(1)
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
    else:
        with open('data.json', 'r') as file:
            data = json.load(file)
        data['failed'].append(1)
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # BEFORE SUITE
    json_temp = {
        "other": [],
        "failed": [],
        "success": []
    }
    jsonString = json.dumps(json_temp)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    yield
    # AFTER SUITE