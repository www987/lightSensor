#!/usr/bin/python
import time
from TSL2581 import TSL2581


"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([LightSensor()])


class LightSensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Light sensor example"
    _attr_native_unit_of_measurement = TEMP_CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        Light=TSL2581(0X39, debug=False)

        id=Light.Read_ID() & 0xf0
        print('ID = %#x'%id)
        Light.Init_TSL2581()

        #while True:
        lux  =  Light.calculate_Lux(2, 148)
        self._attr_native_value = lux
        print('lux = %#d'%lux)
        #time.sleep(1)

        # GPIO.cleanup()
        print ("\nProgram end")
        exit()
        
