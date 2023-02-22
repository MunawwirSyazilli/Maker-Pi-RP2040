from machine import Pin, ADC
import time

# digital output light sensor
digital_sensor_pin = Pin(2, Pin.IN)

while True:
    # read digital sensor value
    digital_value = digital_sensor_pin.value()
    print("Digital value: ", digital_value)

    # wait for 0.5 second
    time.sleep(0.5)
