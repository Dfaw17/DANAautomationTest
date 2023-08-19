import random
import requests
from faker import Faker
from api.setting import general

# ======================================== HOST ========================================
host_gorest = "https://gorest.co.in/public/v2"

# ======================================== ENDPOINT ========================================
api_user = host_gorest + "/users"


# ======================================== MODELS ========================================
def get_list_users():
    req = requests.get(api_user)
    return req


def create_user(random_name, gender, random_email, status):
    payload = {
        "name": random_name,
        "gender": gender,
        "email": random_email,
        "status": status
    }
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": general.berear_token,
    }
    req = requests.post(api_user, json=payload, headers=head)
    return req


def update_user(user_id, random_name, gender, status):
    payload = {
        "name": random_name,
        "gender": gender,
        "status": status
    }
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": general.berear_token,
    }
    req = requests.patch(api_user + f"/{user_id}", json=payload, headers=head)
    return req


def delete_user(user_id):
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": general.berear_token,
    }
    req = requests.delete(api_user + f"/{user_id}", headers=head)
    return req
