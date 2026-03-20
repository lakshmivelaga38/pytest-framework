import allure
from utils.allure_helper import attach_request, attach_response

@allure.feature("GET User")
def test_get_user(api_client):
    endpoint = "/users/2"
    attach_request(endpoint, {})
    response = api_client.request("GET", endpoint)
    attach_response(response)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

@allure.feature("Create User")
def test_create_user(api_client):
    payload = {"name": "Sonal", "job": "QA"}
    attach_request("/users", payload)
    response = api_client.request("POST", "/users", payload)
    attach_response(response)
    assert response.status_code == 201
    assert "id" in response.json()

@allure.feature("Update User")
def test_update_user(api_client):
    payload = {"name": "Updated", "job": "Lead"}
    attach_request("/users/2", payload)
    response = api_client.request("PUT", "/users/2", payload)
    attach_response(response)
    assert response.status_code == 200

@allure.feature("Delete User")
def test_delete_user(api_client):
    attach_request("/users/2", {})
    response = api_client.request("DELETE", "/users/2")
    attach_response(response)
    assert response.status_code == 204
