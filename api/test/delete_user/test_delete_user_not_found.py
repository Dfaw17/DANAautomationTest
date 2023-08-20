import pytest
from assertpy import assert_that
from api.setting.endpoint import *
from api.setting.general import *
from api.json_schema.schema_response_gorest import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(21)
def test():
    # REQUEST
    req = delete_user("112233")
    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_message = req.json().get("message")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(404)
    assert_that(verify_latency).is_less_than(max_latency)
    assert_that(verify_message).is_equal_to("Resource not found")
