from machine import ADC
import time 


# ----- Pin setup (as per your table) -----
# AO  -> pin 31 = GP26 = ADC0  (through 10k/15k resistors)
# DO  -> not connected
# GND -> pin 38
# VCC -> pin 40 (VBUS 5V)
gas_sensor = ADC(26)

#-----SETTING-----
VREF = 3.3
DIVIDER = (10_000+15_000)/15_000

print("gaas sensor test started")
print("Wait 1-2 minutes for the sensor to warm up")

while True:
  raw = gas_sensor.read_u16()
  pin_voltage = raw * VREF/65535 #voltage at pico pin 31
  sensor_voltage = pin_voltage * DIVIDER

  print("Raw", raw, "|Pico pin V:", round(pin_voltage, 2),
        "|Sensor V:", round(sensor_voltage, 2))

  time.sleep(1)