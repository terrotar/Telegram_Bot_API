import pytest
import requests


# Tests of route /api/all_users


# Test of a success request/response
def test_get_all_users():
    response = requests.get("http://127.0.0.1:5000/api/all_users")
    assert response.status_code == 200


# Route /user/get/<id_user>


# Tests of success request/response
def test_get_success_user():
    id_user = 1953480767
    response = requests.get(f"http://127.0.0.1:5000/api/user/get/{id_user}")
    assert response.status_code == 200


# Tests of wrong id_user
def test_get_wrong_id_user():
    id_user = 666
    response = requests.get(f"http://127.0.0.1:5000/api/user/get/{id_user}")
    assert response.status_code == 400


# Route /user/message/<user_id>/<message>


# Tests of success request/response
def test_post_success_user():
    user_id = 1953480767
    message = "Test message with sucess"
    response = requests.get(f"http://127.0.0.1:5000/api/user/message/{user_id}/{message}")
    assert response.status_code == 200


# Tests of wrong id_user
def test_post_wrong_id_user():
    user_id = 666
    message = "Test message failed"
    response = requests.get(f"http://127.0.0.1:5000/api/user/message/{user_id}/{message}")
    assert response.status_code == 400
