# UNBWeatherStation

As a part of the Margot Roach Internship at UNB, we built a Raspberry Pi WeatherStation and collected temperature, humidity, and pressure data at various different altitudes to measure the adiabatic lapse rate of the region.

# Implementation

The station consisted of a BME280 (environement sensor) and a DS3231 (Real Time Clock). The RTC was to compensate for the lack of a externally-powered clock in the RPi, allowing it to retain the correct time even after an extended period of time powered off. The station was programmed to begin recording measurements on startup, for 5-8 minutes depending on the setting of the device.

# Development

Using SSH, we remotely connected to the Raspberry Pi's and used Git for version control. The scripts were mainly in Python and Bash.

# Results and Error

Below are our measured lapse rates:

| Rate ($\degree$ C / km) | Uncertainty for Lapse Rate (Error Propagation) |
| ----------------------- | ---------------------------------------------- |
| 5.40                    | $\pm$ 3.08                                     |
| 7.76                    | $\pm$ 3.09                                     |
| 12.71                   | $\pm$ 3.10                                     |
| 16.02                   | $\pm$ 3.12                                     |
| 19.57                   | $\pm$ 3.14                                     |

The final average was $12.3 \pm 1.4 \degree C \cdot km^{-1}$, which fell significantly out of bounds of the theoretical maximum.

We concluded that this was the result of too small of an altitude difference (45m) which greately magnified the errors, producing an inaccurate result.

## Plotted Results

The orange and green lines are the theoretical max and min, respectively.
![LapseRateGraph](https://github.com/vichua2006/UNBWeatherStation/blob/main/LapseRateGraph.png)
