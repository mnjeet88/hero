from utils.logger import get_logger

logger = get_logger()


def assert_status_code(response, expected_code):
    actual = response.status_code
    logger.info(f"Asserting Status Code: Expected={expected_code}, Actual={actual}")

    assert actual == expected_code, \
        f"Expected status code {expected_code}, but got {actual}. Response: {response.text}"


def assert_field_equal(response_json, field, expected_value):
    actual_value = response_json.get(field)

    logger.info(f"Asserting Field: {field} | Expected={expected_value}, Actual={actual_value}")

    assert actual_value == expected_value, \
        f"Mismatch in field '{field}': Expected={expected_value}, Actual={actual_value}"
