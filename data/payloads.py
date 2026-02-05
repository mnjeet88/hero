def create_booking_payload(firstname, lastname, price=150):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": price,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-10"
        },
        "additionalneeds": "Breakfast"
    }


def update_booking_payload():
    return {
        "firstname": "UpdatedName",
        "lastname": "UpdatedLast",
        "totalprice": 250,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-02-01",
            "checkout": "2026-02-05"
        },
        "additionalneeds": "Lunch"
    }


def auth_payload():
    return {
        "username": "admin",
        "password": "password123"
    }
