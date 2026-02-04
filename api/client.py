import requests
from utils.logger import get_logger

logger = get_logger()


class APIClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET Request: {url}")
        response = requests.get(url, headers=headers, timeout=self.timeout)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response

    def post(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST Request: {url}")
        logger.info(f"Payload: {payload}")
        response = requests.post(url, json=payload, headers=headers, timeout=self.timeout)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response

    def put(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT Request: {url}")
        logger.info(f"Payload: {payload}")
        response = requests.put(url, json=payload, headers=headers, timeout=self.timeout)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE Request: {url}")
        response = requests.delete(url, headers=headers, timeout=self.timeout)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response
