
###########################
#Test case
#1. test_get_users_status_code()
#    Requirement covered- Successful response
#    Expected result -HTTP 200
# 2. test_get_users_response_content()
#     Requirement covered - Validate response content
#     Expected result - data key exists and contains a list
# 3.test_get_single_user()
#    Requirement covered -Validate a specific value
#    Expected result - User ID equals 2
# 4.test_get_invalid_user()
#    Requirement covered - Error handling
#    Expected result - HTTP 404 for a nonexistent user
###############
# Author: Asha M
# Date: Oct 23rd, 2026
################################
#
# Copyright 2026 DAVE AI ,Bangalore
#
###############################

import pytest
import requests

BASE_URL = "https://reqres.in/api"
API_KEY = "pub_de2fefdb0de2f9bb8de92b0722a7828db635d67f05c49152caffa27c59cb983a"

HEADERS = {
    "x-api-key": API_KEY
}
response = requests.get(
    f"{BASE_URL}/users?page=2",
    headers=HEADERS,
    timeout=15
)
def test_get_users_status_code():
    """Test 1: Verify successful response status code."""
    response = requests.get(
        f"{BASE_URL}/users?page=2",
        timeout=15
    
    )

    assert response.status_code == 200

def test_get_users_response_content():
    """Test 2: Validate response content."""
    response = requests.get(
        f"{BASE_URL}/users?page=2",
        timeout=15
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

    if data["data"]:
        assert "id" in data["data"][0]
        assert "email" in data["data"][0]


def test_get_single_user():
    """Test 3: Validate a specific user's details."""
    response = requests.get(
        f"{BASE_URL}/users/2",
        timeout=15
    )

    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"


def test_get_invalid_user():
    """Test 4: Verify error handling for a nonexistent user."""
    response = requests.get(
        f"{BASE_URL}/users/9999",
        timeout=15
    )

    assert response.status_code == 404
