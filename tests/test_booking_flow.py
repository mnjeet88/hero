import pytest
from api import endpoints
from data.payloads import create_booking_payload, update_booking_payload
from data.testdata import CREATE_BOOKING_DATA
from data.assertions_data import EXPECTED_UPDATE_VALUES
from utils.assertions import assert_status_code, assert_field_equal
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.parametrize("firstname, lastname", CREATE_BOOKING_DATA)
def test_create_booking(api_client, firstname, lastname):
    logger.info("===== TEST: CREATE BOOKING =====")

    payload = create_booking_payload(firstname, lastname)

    response = api_client.post(endpoints.BOOKING, payload)

    assert_status_code(response, 200)

    data = response.json()

    booking_id = data["bookingid"]
    booking = data["booking"]

    logger.info(f"Created Booking ID: {booking_id}")
    logger.info(f"Created Booking Details: {booking}")

    assert_field_equal(booking, "firstname", firstname)
    assert_field_equal(booking, "lastname", lastname)

    pytest.booking_id = booking_id


def test_get_booking(api_client):
    logger.info("===== TEST: GET BOOKING =====")

    booking_id = pytest.booking_id

    response = api_client.get(f"{endpoints.BOOKING}/{booking_id}")

    assert_status_code(response, 200)

    data = response.json()

    logger.info(f"Retrieved Booking Data: {data}")

    assert "firstname" in data, "firstname field missing in response"
    assert "lastname" in data, "lastname field missing in response"


def test_update_booking(api_client, auth_headers):
    logger.info("===== TEST: UPDATE BOOKING WITH AUTH =====")

    booking_id = pytest.booking_id

    payload = update_booking_payload()

    response = api_client.put(
        f"{endpoints.BOOKING}/{booking_id}",
        payload,
        headers=auth_headers
    )

    assert_status_code(response, 200)

    updated = response.json()

    logger.info(f"Updated Booking Data: {updated}")

    # assert_field_equal(updated, "firstname", "UpdatedName")
    # assert_field_equal(updated, "totalprice", 250)
    for key, value in EXPECTED_UPDATE_VALUES.items():
        assert_field_equal(updated, key, value)


def test_delete_booking(api_client, auth_headers):
    logger.info("===== TEST: DELETE BOOKING WITH AUTH =====")

    booking_id = pytest.booking_id

    response = api_client.delete(
        f"{endpoints.BOOKING}/{booking_id}",
        headers=auth_headers
    )

    assert_status_code(response, 201)

    logger.info("Booking deleted successfully")

    response = api_client.get(f"{endpoints.BOOKING}/{booking_id}")

    logger.info("Trying to fetch deleted booking")

    assert_status_code(response, 404)
