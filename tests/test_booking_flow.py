import pytest
from api import endpoints
from utils.assertions import assert_status_code, assert_field_equal
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.parametrize("firstname, lastname", [
    ("Manjeet", "Mohan"),
    ("Sally", "Brown"),
])
def test_create_booking(api_client, firstname, lastname):
    logger.info("===== TEST: CREATE BOOKING =====")

    payload = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-02-04",
            "checkout": "2026-01-5"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_client.post(endpoints.BOOKING, payload)

    assert_status_code(response, 200)

    data = response.json()

    booking_id = data["bookingid"]
    booking = data["booking"]

    logger.info(f"Created Booking ID: {booking_id}")
    logger.info(f"Created Booking Details: {booking}")

    assert_field_equal(booking, "firstname", firstname)
    assert_field_equal(booking, "lastname", lastname)

    pytest.booking_id = data["bookingid"]


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

    payload = {
        "firstname": "UpdatedName",
        "lastname": "UpdatedLast",
        "totalprice": 250,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-03-01",
            "checkout": "2026-03-05"
        },
        "additionalneeds": "Lunch"
    }

    response = api_client.put(
        f"{endpoints.BOOKING}/{booking_id}",
        payload,
        headers=auth_headers
    )

    assert_status_code(response, 200)

    updated = response.json()

    logger.info(f"Updated Booking Data: {updated}")

    assert_field_equal(updated, "firstname", "UpdatedName")
    assert_field_equal(updated, "totalprice", 250)


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
