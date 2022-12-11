
class LengthUnit:
    """
    Enum representing length units.
    """
    Milimeter = 1
    Centimeter = 2
    Meter = 3
    Inch = 4


def ultrasonic_cast(lengthUnit):
    """
    Converts unit to constant used in calculations for ultrasonic distance sensor.

    :param lengthUnit: Unit class object.
    :return: Constant for ultrasonic sensor.
    """
    if lengthUnit == 2:
        return 58
    if lengthUnit == 3:
        return 5800
    if lengthUnit == 4:
        return 148
    return 5.8
