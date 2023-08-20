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
    status = "actiff"
    req = create_user(random_name, gender, random_email, status)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_message = req.json()[0].get("message")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(422)
    assert_that(verify_latency).is_less_than(max_latency)
    assert_that(verify_message).is_equal_to("can't be blank")
