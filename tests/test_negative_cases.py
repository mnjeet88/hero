from api import endpoints
from data.testdata import INVALID_BOOKING_ID
from utils.assertions import assert_status_code
from utils.logger import get_logger

logger = get_logger()


def test_get_non_existing_booking(api_client):
    logger.info("===== NEGATIVE TEST: GET INVALID BOOKING =====")

    response = api_client.get(f"{endpoints.BOOKING}/{INVALID_BOOKING_ID}")

    logger.info(f"Response for invalid booking: {response.text}")

    assert_status_code(response, 404)


def test_update_without_auth(api_client):
    logger.info("===== NEGATIVE TEST: UPDATE WITHOUT AUTH =====")

    payload = {"firstname": "Hacker"}

    response = api_client.put(f"{endpoints.BOOKING}/1", payload)

    # logger.info(f"Update without auth response: {response.text}")
    #
    # assert_status_code(response, 403)
    assert response.status_code in [403, 405], \
        f"Expected 403 or 405 but got {response.status_code}"


def test_delete_invalid_id(api_client, auth_headers):
    logger.info("===== NEGATIVE TEST: DELETE INVALID ID =====")

    response = api_client.delete(
        f"{endpoints.BOOKING}/{INVALID_BOOKING_ID}",
        headers=auth_headers
    )

    logger.info(f"Delete invalid id response: {response.text}")

    assert_status_code(response, 405)
