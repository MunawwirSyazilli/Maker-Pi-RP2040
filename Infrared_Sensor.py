from machine import Pin
import time

# digital input IR sensor
ir_sensor_pin = Pin(2, Pin.IN)

while True:
    # read IR sensor value
    ir_value = ir_sensor_pin.value()
    print("IR value: ", ir_value)

    # wait for 30 second
    time.sleep(0.5)
