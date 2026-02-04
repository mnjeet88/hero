import pytest
from api.client import APIClient
from api import endpoints
from utils.logger import get_logger

logger = get_logger()

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def api_client():
    logger.info("Initializing API Client")
    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def auth_token(api_client):
    logger.info("Generating Auth Token")

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = api_client.post(endpoints.AUTH, payload)

    assert response.status_code == 200, "Auth Token generation failed"

    token = response.json()["token"]

    logger.info(f"Auth Token Generated: {token}")

    return token


@pytest.fixture
def auth_headers(auth_token):
    return {
        "Cookie": f"token={auth_token}",
        "Content-Type": "application/json"
    }
