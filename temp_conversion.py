"""
A module for converting temperature from Imperial to Metric units.
Will throw ValueErrors for temperatures < absolute zero.

Functions:
    convert_fahr_to_celsius: Converts Fahrenheit to Celsius
    convert_fahr_to_kelvin: Converts Fahrenheit to Kelvin
"""


def convert_fahr_to_celsius(fahr):
    """
    Given a temperature in Fahrenheit, converts it to Celsius

    :param fahr: The temperature in Fahrenheit
    :raises ValueError: If the temperature is below absolute zero
    :return: The temperature in Celsius
    """
    temp_celsius = (fahr - 32) * (5 / 9)
    # If temperature is below absolute zero, throw an error
    if temp_celsius < -273.15:
            raise ValueError(f"Trying to convert impossible temperature: {fahr}F")
    return temp_celsius

def convert_fahr_to_kelvin(fahr):
    """
    Given a temperature in Fahrenheit, converts it to Kelvin

    :param fahr: The temperature in Fahrenheit
    :return: The temperature in Kelvin
    """
    temp_celsius = convert_fahr_to_celsius(fahr)
    temp_kelvin = temp_celsius + 273.15
    return temp_kelvin
