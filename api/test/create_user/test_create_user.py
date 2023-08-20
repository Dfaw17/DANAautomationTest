import pytest
from assertpy import assert_that
from api.setting.endpoint import *
from api.setting.general import *
from api.json_schema.schema_response_gorest import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(20)
def test():

    # REQUEST
    fake = Faker()
    random_num = random.randint(0, 1000)
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_email = f"{first_name}{last_name}{random_num}@gmail.com"
    random_name = f"{first_name} {last_name}"
    gender = "male"
    status = "active"
    req = create_user(random_name, gender, random_email, status)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_id = req.json().get("id")
    verify_name = req.json().get("name")
    verify_email = req.json().get("email")
    verify_gender = req.json().get("gender")
    verify_status = req.json().get("status")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(201)
    assert_that(verify_latency).is_less_than(max_latency)
    validate_json_schema(instance=req.json(), schema=create_user_normal)
    assert_that(verify_id).is_not_none()
    assert_that(verify_name).is_equal_to(random_name)
    assert_that(verify_email).is_equal_to(random_email)
    assert_that(verify_gender).is_equal_to(gender)
    assert_that(verify_status).is_equal_to(status)
