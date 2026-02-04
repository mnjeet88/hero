from api import endpoints
from utils.assertions import assert_status_code
from utils.logger import get_logger

logger = get_logger()


def test_get_non_existing_booking(api_client):
    logger.info("===== NEGATIVE TEST: GET INVALID BOOKING =====")

    response = api_client.get(f"{endpoints.BOOKING}/999999")

    logger.info(f"Response for invalid booking: {response.text}")

    assert_status_code(response, 404)


def test_update_without_auth(api_client):
    logger.info("===== NEGATIVE TEST: UPDATE WITHOUT AUTH =====")

    payload = {"firstname": "Hacker"}

    response = api_client.put(f"{endpoints.BOOKING}/1", payload)

    logger.info(f"Update without auth response: {response.text}")

    assert_status_code(response, 403)


def test_delete_invalid_id(api_client, auth_headers):
    response = api_client.delete(
        f"{endpoints.BOOKING}/999999",
        headers=auth_headers
    )

    assert_status_code(response, 405)
