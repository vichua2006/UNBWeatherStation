# #!/bin/bash


# for the RTC; must be before the script to have accurate time
echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
sudo hwclock -s