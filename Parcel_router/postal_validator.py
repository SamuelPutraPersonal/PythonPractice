# postal_validator.py

# This list simulates PostNL's knowledge of "standard" postal code prefixes.
# In a real system, this would be a much larger, dynamic database.
# Dutch postal codes are 4 digits followed by 2 letters (e.g., 1234 AB)
# We'll simplify and just check the first two digits for "standard" areas.
STANDARD_POSTAL_CODE_PREFIXES = [
    "10",
    "11",
    "20",
    "25",
    "30",
    "35",
    "40",
    "50",
    "60",
    "70",
    "80",
    "90",
]


def validate_dutch_postal_code(postal_code: str) -> str:
    """
    Simulates a PostNL system checking if a postal code is for a standard delivery area.

    Args:
        postal_code (str): A Dutch postal code (e.g., "1234 AB").

    Returns:
        str: "Standard Delivery" if valid and in a standard area,
             "Special Handling" otherwise.
    """
    # Basic format check (very simplified for this example)
    if not isinstance(postal_code, str) or len(postal_code) < 4:
        return "Special Handling (Invalid Format)"

    # Extract the numeric part (first 4 digits)
    numeric_part = postal_code[:4]

    # Check if the first two digits are in our list of standard prefixes
    if numeric_part[:2] in STANDARD_POSTAL_CODE_PREFIXES:
        return "Standard Delivery"
    else:
        return "Special Handling (Non-Standard Area)"


# --- Mock Parcel Data (for demonstration) ---
mock_parcels_for_validation = [
    {"id": "P001", "postal_code": "1012 AB"},  # Standard Amsterdam
    {"id": "P002", "postal_code": "2514 CD"},  # Standard The Hague
    {
        "id": "P003",
        "postal_code": "9999 ZZ",
    },  # Non-standard (e.g., very remote or invalid)
    {
        "id": "P004",
        "postal_code": "0123 AB",
    },  # Non-standard (leading zero, not in our list)
    {"id": "P005", "postal_code": "123"},  # Invalid format (too short)
    {"id": "P006", "postal_code": "6000 AA"},  # Standard Limburg
    {"id": "P007", "postal_code": ""},  # Empty string
    {"id": "P008", "postal_code": None},  # None value
]

# --- Running the System (Simple Simulation) ---
if __name__ == "__main__":
    print("--- PostNL Postal Code Validator Simulation ---")
    print("This mimics a very simple part of PostNL's parcel routing decisions.")

    for parcel in mock_parcels_for_validation:
        parcel_id = parcel.get("id", "N/A")
        postal_code = parcel.get("postal_code")

        # Call the developer's function
        validation_result = validate_dutch_postal_code(postal_code)

        print(
            f"Parcel ID: {parcel_id}, Postal Code: '{postal_code}' -> Result: {validation_result}"
        )

    print("---------------------------------------------")
