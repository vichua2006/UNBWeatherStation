import os
from dotenv import load_dotenv

load_dotenv()

# Load device name and calibration 
device_name = os.getenv("NAME")
TEMP_CALI = os.getenv("TEMP_CALI")
PRESSURE_CALI = os.getenv("PRESSURE_CALI")
HUMIDITY_CALI = os.getenv("HUMIDITY_CALI")

print(device_name, TEMP_CALI, PRESSURE_CALI, HUMIDITY_CALI)