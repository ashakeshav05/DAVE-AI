
# #########################################
# Test Case = Website Testing

# Objective:
# Demonstrate your ability to write automated tests for both APIs and web applications
# using Python. The assignment will assess your understanding of test case design, test
# execution, and basic automation practices..
# Main Steps:
# 1. Open the Chrome browser
# 2. Navigate to https://www.iamdave.ai/
#Verify that the website loads successfully and displays the expected title or logo.
#Test a navigation flow (e.g. click a link/button and verify a new page opens).
#Test a form submission or input field interaction if available.
#Check for the presence of a specific element on the homepage (e.g. a heading, button, or image)
#Requirements:
#Used Python with Selenium WebDriver.
#Used any browser driver ChromeDriver
# Author: Asha M
# Date: Oct 23rd, 2026
################################
#
# Copyright 2026 DAVE AI ,Bangalore
#
###############################

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.iamdave.ai/"
CONTACT_URL = "https://www.iamdave.ai/contact-us/"
PLATFORM_URL = "https://www.iamdave.ai/platform/"


def _setup():
    """Set up Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)

    print("\nSetup: Chrome browser launched")
    return browser


def teardown(browser):
    """Close Chrome WebDriver."""
    if browser:
        browser.quit()
        print("Teardown: Chrome browser closed")


@pytest.fixture
def driver():
    """Run setup before and teardown after each test."""
    browser = _setup()
    try:
        yield browser
    finally:
        teardown(browser)


def test_homepage_loads_successfully(driver):
    """TC01: Verify homepage loads and displays its heading."""
    print("Executing TC01: Homepage validation")

    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )

    assert driver.title.strip() != ""

    heading = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                '//*[@id="main"]/div/section[1]/div/div/div/section/div/div[1]/div/div[1]/div/h1'
            )
        )
    )

    assert "Automotive Intelligence Across Every Function" in heading.text


def test_platform_navigation(driver):
    """TC02: Verify navigation to the Platform page."""
    print("Executing TC02: Platform navigation")

    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 20)

    platform_link = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'a[href="{PLATFORM_URL}"]')
        )
    )

    platform_link.click()

    wait.until(EC.url_contains("/platform/"))

    assert "/platform/" in driver.current_url.lower()


def test_contact_form_fields_are_visible(driver):
    """TC03: Verify contact form fields are displayed."""
    print("Executing TC03: Contact form field validation")

    driver.get(CONTACT_URL)
    wait = WebDriverWait(driver, 20)

    placeholders = [
        "Name",
        "Email",
        "Company name",
        "Phone number"
    ]

    for placeholder in placeholders:
        field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    f'input[placeholder="{placeholder}"]'
                )
            )
        )

        assert field.is_displayed()


def test_contact_form_accepts_input(driver):
    """TC04: Verify contact form accepts user input."""
    print("Executing TC04: Contact form input validation")

    driver.get(CONTACT_URL)
    wait = WebDriverWait(driver, 20)

    test_data = {
        "Name": "Asha M",
        "Email": "ashakeshav74@gmail.com",
        "Company name": "Adv",
        "Phone number": "7483935382"
    }

    for placeholder, value in test_data.items():
        field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    f'input[placeholder="{placeholder}"]'
                )
            )
        )

        field.clear()
        field.send_keys(value)

        assert field.get_attribute("value") == value
