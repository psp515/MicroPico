
class LengthUnit:
    """
    Enum representing length units.
    """
    Milimeter = 1
    Centimeter = 2
    Meter = 3
    Inch = 4


def get_lengthunit_shortname(unit:LengthUnit):
    if unit == LengthUnit.Milimeter:
        return "mm"
    if unit == LengthUnit.Centimeter:
        return "cm"
    if unit == LengthUnit.Meter:
        return "m"

    return "in"

