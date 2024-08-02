import os
import time
import pytz
import datetime
import smbus2
import bme280
from dotenv import load_dotenv

# BME280 sensor address (default address)
address = 0x77

# Initialize I2C bus
bus = smbus2.SMBus(0)

# Load calibration parameters (basically specifying a sensor)
calibration_params = bme280.load_calibration_params(bus, address)

# Load timezone 
halifax_tz = pytz.timezone("America/Halifax")

# Load env variables
load_dotenv()

# Load device name and calibration 
device_name = os.getenv("NAME")
USERNAME = str(os.getenv("USERNAME"))
TEMP_CALI = float(os.getenv("TEMP_CALI"))
PRESSURE_CALI = float(os.getenv("PRESSURE_CALI"))
HUMIDITY_CALI = float(os.getenv("HUMIDITY_CALI"))

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():

    header = [
        "Time",
        "Temperature (C)",
        "Pressure (hPa)",
        "Humidity",
    ]

    # Init csv file header
    date = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M") 
    with open(rf"/home/{USERNAME}/Desktop/UNBWeatherStation/data/{date}_{device_name}.csv", "w") as file:
        header_str = ",".join(header)
        file.write(header_str + "\n")

        # main loop
        for i in range(420):
            try:
                # Read sensor data
                data = bme280.sample(bus, address, calibration_params)

                # Extract temperature, pressure, and humidity
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                temperature_celsius = data.temperature + TEMP_CALI
                pressure = data.pressure + PRESSURE_CALI
                humidity = data.humidity + HUMIDITY_CALI

                # Convert temperature to Fahrenheit
                # temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

                # write the measurements to the csv file
                reading_str = ",".join([str(x) for x in [
                    timestamp,
                    temperature_celsius,
                    pressure,
                    humidity,
                ]])

                file.write(reading_str)
                file.write("\n")

                print(reading_str)

                # Wait for a few seconds before the next reading
                time.sleep(1)

            except KeyboardInterrupt:
                print('Program stopped')
                break
            except Exception as e:
                print('An unexpected error occurred:', str(e))
                break

if (__name__ == "__main__"):
    time.sleep(30) # wait for system to be set to RTC clock
    main()
