class Unit:
    Meter = 1
    Centimeter = 2
    Inch = 3



def ultrasonic_cast(value):
    if value == 1:
        return 5800

    if value == 2:
        return 58

    return 148