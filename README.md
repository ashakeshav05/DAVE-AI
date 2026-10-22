# DAVE-AI
Demonstrate your ability to write automated tests for both APIs and web applications using Python. The assignment will assess your understanding of test case design, test execution, and basic automation practices.
# ReqRes API Testing Assignment

**Author:** Asha M\
**Date:** October 23, 2026

## 1. Project Overview

QA Engineer Assignment

Objective:
Demonstrate your ability to write automated tests for both APIs and web applications
using Python. The assignment will assess your understanding of test case design, test
execution, and basic automation practices.

Part 1: API Testing
Pick the publicly available API Reqres
Tasks:
Write 3–4 test cases using Python’s unittest or pytest framework.
At least one test case should:
Validate a successful response (status code 200).
Validate response content, e.g., a key exists or a value is correct.
Validate error handling, e.g., missing or invalid parameters.
Optional Bonus:
Implement Locust to run a simple load test on one of the API endpoints.
Include a test plan with simulated user loads and record results.
Limit this to a max of 100 api calls within the day, so you may be able to test a load of up
to 5to10 concurrent users
Part 2: Website Testing
Test the website: www.iamdave.ai
Tasks:
Write 3–4 Selenium/Playwright/Cypress test cases using Python to automate UI tests.
Examples of tests you could include:
Verify that the website loads successfully and displays the expected title or logo.
Test a navigation flow (e.g. click a link/button and verify a new page opens).
Test a form submission or input field interaction if available.
Check for the presence of a specific element on the homepage (e.g. a heading, button, or
image).
Requirements:
Use Python with Selenium/Playwright/Cypress WebDriver.
Use any browser driver you prefer (e.g. ChromeDriver).
Include clear setup and teardown steps in your test scripts.

## 2. Tools and Technologies

-   Python
-   `pytest` --- test framework
-   `requests` --- sends HTTP requests
-   ReqRes API --- API under test
-   PyCharm --- Python IDE

## 3. API Under Test

Base URL:

``` text
https://reqres.in/api
```

Endpoints used:

  Method   Endpoint          Purpose
  -------- ----------------- --------------------------------------
  GET      `/users?page=2`   Retrieve a page of users
  GET      `/users/2`        Retrieve user ID 2
  GET      `/users/9999`     Check handling of a nonexistent user

Replace `YOUR_PUBLIC_API_KEY` locally with your own valid public API
key. Do not paste the real key into this README or upload it to a public
repository.

## 5. Setup

### Install dependencies

Open the PyCharm terminal and run:

``` bash
python -m pip install pytest requests
```

### Configure the API key

In `test_api.py`, configure the base URL and header:

``` python
BASE_URL = "https://reqres.in/api"
API_KEY = "YOUR_PUBLIC_API_KEY"

HEADERS = {
    "x-api-key": API_KEY
}
```

Ensure every API request includes `headers=HEADERS`.

## 6. Run the Tests

Run all tests from the project directory:

``` bash
python -m pytest -s -v test_api.py
```

-   `-v` displays each test name and its result.
-   `-s` displays `print()` output from the tests.

A passing test is reported as `PASSED`; a failed assertion is reported
as `FAILED`. Results depend on the API's current behavior,
authentication requirements, and rate limits.


