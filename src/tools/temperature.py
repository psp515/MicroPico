from src.enums.temperature_units_enum import TemperatureUnit


class Temperature:
    """
    Represents tempearture with unit
    """
    _temperature: float
    _unit: TemperatureUnit

    def __init__(self, temperature: float, unit: TemperatureUnit):
        self._temperature = temperature
        self._unit = unit

    # TODO : some base functions