import pytest
from assertpy import assert_that
from api.setting.endpoint import *
from api.setting.general import *
from api.json_schema.schema_response_gorest import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(33)
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
    payload = {
        "name": random_name,
        "gender": gender,
        "email": random_email,
        "status": status
    }
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "AABBCCDD",
    }
    req = requests.post(api_user, json=payload, headers=head)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_message = req.json().get("message")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(401)
    assert_that(verify_latency).is_less_than(max_latency)
    assert_that(verify_message).is_equal_to("Authentication failed")
