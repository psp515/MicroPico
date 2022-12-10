class Unit:
    Milimeter = 1
    Centimeter = 2
    Meter = 3
    Inch = 4


def ultrasonic_cast(unit):
    """
    Converts unit to constant used in calculations for ultrasonic distance sensor.

    :param unit: Unit class object.
    :return: Constant for ultrasonic sensor.
    """
    if unit == 2:
        return 58
    if unit == 3:
        return 5800
    if unit == 4:
        return 148
    return 5.8
