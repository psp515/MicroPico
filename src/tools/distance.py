from src.enums.length_units_enum import LengthUnit, get_lengthunit_shortname


class Distance:
    """
    Class for representing value distance with unit.
    """
    _distance: float
    _unit: LengthUnit

    def __init__(self, distance: float, unit: LengthUnit):
        """
        Initializes distance object.

        :param distance: Distance.
        :param unit: Distance unit.
        """
        self._unit = unit
        self._distance = distance

    @property
    def unit(self):
        """
        :return: Object unit.
        """
        return self._unit

    @property
    def distance(self):
        """
        :return: Distance value.
        """
        return self._distance

    def __str__(self):
        return f"{self._distance} {get_lengthunit_shortname(self._unit)}"

    def change_unit(self, unit: LengthUnit, precision: int = 1):
        pass

