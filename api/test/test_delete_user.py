import pytest
from assertpy import assert_that
from api.setting.endpoint import *
from api.setting.general import *
from api.json_schema.schema_response_gorest import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(21)
def test_delete_user_normal():

    # REQUEST
    fake = Faker()
    random_num = random.randint(0, 1000)
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_email = f"{first_name}{last_name}{random_num}@gmail.com"
    random_name = f"{first_name} {last_name}"
    gender = "male"
    status = "active"
    hit_create_user = create_user(random_name, gender, random_email, status)
    user_id = hit_create_user.json().get("id")

    req = delete_user(user_id)
    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds

    # ASSERT
    assert_that(verify_status_code).is_equal_to(204)
    assert_that(verify_latency).is_less_than(max_latency)