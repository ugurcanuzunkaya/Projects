def inchestometers(feet, inches):
    """
    This function converts feet and inches to meters.
    1 foot = 12 inches
    1 inch = 0.0254 meters

    Parameters:
    feet (int): The number of feet to be converted.
    inches (int): The number of inches to be converted.

    Returns:
    float: The number of meters after conversion. Precision is 4 decimal places.
    """
    feet_to_inches = feet * 12
    total_inches = feet_to_inches + inches
    return round((total_inches * 0.0254), 4)


if __name__ == "__main__":
    # Test the function
    print(inchestometers(5, 8))  # 1.7272

    assert inchestometers(5, 8) == 1.7272
    assert inchestometers(6, 0) == 1.8288
