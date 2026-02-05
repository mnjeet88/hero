# Pytest API Automation Framework

## Overview

This framework automates API testing for the Restful Booker application using Python, Pytest, and Requests.

## System Under Test

Base URL:  
https://restful-booker.herokuapp.com

API Documentation:  
https://restful-booker.herokuapp.com/apidoc

---

## Framework Features

- Modular and reusable API client  
- Centralized test data  
- Separated API payload definitions  
- Externalized assertion values  
- Pytest fixtures for authentication  
- Parametrized test execution  
- Detailed logging  
- HTML reporting  

---

## Folder Structure

- api/ – API client and endpoints  
- data/ – Test data, payloads, expected assertions  
- tests/ – Test cases  
- utils/ – Logger and assertions  
- conftest.py – Pytest fixtures  

---

## Setup Instructions

### Install dependencies

pip install -r requirements.txt

### Run all tests

pytest

### Run with HTML report

pytest --html=report.html

---


---

## Test Coverage

### Positive Flow

- Create booking  
- Retrieve booking  
- Update booking  
- Delete booking  

### Negative Scenarios

- Fetch non-existing booking  
- Update without auth  
- Delete invalid booking  

---

## How to Extend

- Add new payloads in data/payloads.py  
- Add new test data in data/test_data.py  
- Add new expected values in data/assertions_data.py  
- Write new tests under tests/

---

## Author
Manjeet Mohan
