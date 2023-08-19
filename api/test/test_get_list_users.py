import pytest
from assertpy import assert_that
from api.setting.endpoint import *
from api.setting.general import *
from api.json_schema.schema_response_gorest import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(22)
def test_get_list_user_normal():

    # REQUEST
    random_index = random.randint(0, 9)
    req = get_list_users()

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_resp = req.json()
    verify_gender = req.json()[random_index].get("gender")
    verify_status = req.json()[random_index].get("status")
    verify_email = req.json()[random_index].get("email")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(200)
    assert_that(verify_latency).is_less_than(max_latency)
    validate_json_schema(instance=req.json(), schema=get_list_user_normal)
    assert_that(verify_resp).is_type_of(list)
    assert_that(verify_gender).is_in("female", "male")
    assert_that(verify_status).is_in("active", "inactive")
    assert_that(verify_email).contains("@")
