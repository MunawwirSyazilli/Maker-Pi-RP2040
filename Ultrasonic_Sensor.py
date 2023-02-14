import time
from machine import Pin
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

def measure_distance():
    # Set the trigger pin to HIGH for 10 microseconds
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    
    # Wait for the echo pin to go HIGH
    while echo.value() == 0:
        pass
    
    # Measure the duration of the echo pin being HIGH
    start_time = time.ticks_us()
    while echo.value() == 1:
        pass
    end_time = time.ticks_us()
    
    # Calculate the distance in centimeters
    duration = end_time - start_time
    distance = duration / 58
    
    return distance

while True:
    distance = measure_distance()
    print("Distance: {} cm".format(distance))
    time.sleep(0.1)


