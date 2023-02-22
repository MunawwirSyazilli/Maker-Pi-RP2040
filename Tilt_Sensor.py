from machine import Pin, ADC
import time

# analog input tilt sensor
tilt_sensor_pin = ADC(2)

while True:
    # read tilt sensor value
    tilt_value = tilt_sensor_pin.read()
    print("Tilt value: ", tilt_value)

    # wait for 0.5 second
    time.sleep(0.5)
