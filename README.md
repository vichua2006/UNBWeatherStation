# UNBWeatherStation

As a part of the Margot Roach Internship at UNB, we built a Raspberry Pi WeatherStation and collected temperature, humidity, and pressure data at various different altitudes to measure the adiabatic lapse rate of the region.

# Implementation

The station consisted of a BME280 (environement sensor) and a DS3231 (Real Time Clock). The RTC was to compensate for the lack of a externally-powered clock in the RPi, allowing it to retain the correct time even after an extended period of time powered off. The station was programmed to begin recording measurements on startup, for 5-8 minutes depending on the setting of the device.

# Development

Using SSH, we remotely connected to the Raspberry Pi's and used Git for version control. The scripts were mainly in Python and Bash.
