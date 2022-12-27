
class LengthUnit:
    """
    Enum representing length units.
    """
    MILIMETER = 1
    CENTIMETER = 2
    METER = 3
    INCH = 4


def get_lengthunit_shortname(unit: LengthUnit):
    if unit == LengthUnit.MILIMETER:
        return "mm"
    if unit == LengthUnit.CENTIMETER:
        return "cm"
    if unit == LengthUnit.METER:
        return "m"

    return "in"

