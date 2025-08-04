# test_postal_validator.py

import pytest
from postal_validator import (
    validate_dutch_postal_code,
    STANDARD_POSTAL_CODE_PREFIXES,
)

# --- Test Automation (QA Perspective using pytest) ---

# pytest will automatically find functions that start with 'test_'


def test_standard_postal_code_valid():
    """
    Test Case 1: Verify a standard, valid postal code returns "Standard Delivery".
    (Happy Path)
    """
    postal_code = "1012 AB"  # Example: Amsterdam postal code, starts with "10"
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Standard Delivery"
    ), f"Expected 'Standard Delivery' for {postal_code}, but got '{result}'"
    print(f"Test Passed: {postal_code} routed to Standard Delivery.")


def test_another_standard_postal_code_valid():
    """
    Test Case 2: Verify another standard, valid postal code returns "Standard Delivery".
    (Happy Path)
    """
    postal_code = "6000 AA"  # Example: Limburg postal code, starts with "60"
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Standard Delivery"
    ), f"Expected 'Standard Delivery' for {postal_code}, but got '{result}'"
    print(f"Test Passed: {postal_code} routed to Standard Delivery.")


def test_another_standard_postal_code_valid_2():
    """
    Test case 1: Verify another standard that created by me
    """

    postal_code = "7000 AA"
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Standard Delivery"
    ), f"Expected 'Standard Delivery' for {postal_code}, but got '{result}'"
    print(f"Test Passed: {postal_code} routed to Standard Delivery.")


def test_non_standard_postal_code_numeric_prefix():
    """
    Test Case 3: Verify a postal code with a non-standard numeric prefix returns "Special Handling".
    (Negative Path)
    """
    postal_code = (
        "0123 AB"  # Starts with "01", not in our STANDARD_POSTAL_CODE_PREFIXES
    )
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Special Handling (Non-Standard Area)"
    ), f"Expected 'Special Handling' for {postal_code}, but got '{result}'"
    print(f"Test Passed: {postal_code} routed to Special Handling (Non-Standard Area).")


def test_non_standard_postal_code_numeric():
    """
    Test case 2: verify a postal code with a non-standard numeric
    created by me
    """
    postal_code = "123123123123"
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Special Handling (Non-Standard Area)"
    ), f"Expected 'Special Handling' for {postal_code}, but got '{result}'"
    print(f"Test Passed: {postal_code} routed to Special Handling (Non-Standard Area).")


def test_invalid_short_postal_code_format():
    """
    Test Case 4: Verify an invalid (too short) postal code format returns "Special Handling".
    (Negative Path - Invalid Format)
    """
    postal_code = "123"
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Special Handling (Invalid Format)"
    ), f"Expected 'Special Handling (Invalid Format)' for {postal_code}, but got '{result}'"
    print(f"Test Passed: {postal_code} routed to Special Handling (Invalid Format).")


def test_empty_postal_code():
    """
    Test Case 5: Verify an empty string postal code returns "Special Handling".
    (Edge Case)
    """
    postal_code = ""
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Special Handling (Invalid Format)"
    ), f"Expected 'Special Handling (Invalid Format)' for empty string, but got '{result}'"
    print(
        f"Test Passed: Empty postal code routed to Special Handling (Invalid Format)."
    )


def test_none_postal_code():
    """
    Test Case 6: Verify a None value for postal code returns "Special Handling".
    (Edge Case)
    """
    postal_code = None
    result = validate_dutch_postal_code(postal_code)
    assert (
        result == "Special Handling (Invalid Format)"
    ), f"Expected 'Special Handling (Invalid Format)' for None, but got '{result}'"
    print(f"Test Passed: None postal code routed to Special Handling (Invalid Format).")


def test_long_postal_code_format():
    """
    Test Case 7: Verify a postal code that is too long (but starts with standard prefix)
    still returns "Standard Delivery" based on current simplified logic.
    (Edge Case - highlights where logic could be improved)
    """
    postal_code = "10123456789 AB"  # Too long, but starts with "10"
    result = validate_dutch_postal_code(postal_code)
    # NOTE: In a real system, this should likely be "Special Handling (Invalid Format)"
    # but based on our current simplified logic, it passes the prefix check.
    # This is a good example of how tests reflect current logic, and can highlight areas for refinement.
    assert (
        result == "Standard Delivery"
    ), f"Expected 'Standard Delivery' for {postal_code}, but got '{result}'"
    print(
        f"Test Passed: {postal_code} (long format) routed to Standard Delivery based on prefix."
    )
