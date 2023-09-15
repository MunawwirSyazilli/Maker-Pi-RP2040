import machine
import utime

# Setup DC Motor pins
M1A = machine.PWM(machine.Pin(8))
M1B = machine.PWM(machine.Pin(9))
M2A = machine.PWM(machine.Pin(10))
M2B = machine.PWM(machine.Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

# Setup Ultrasonic sensor pins (HC-SR04)
trigger_pin = machine.Pin(3, machine.Pin.OUT)
echo_pin = machine.Pin(2, machine.Pin.IN)

def measure_distance():
    # Send a 10-microsecond pulse on the trigger pin
    trigger_pin.on()
    utime.sleep_us(10)
    trigger_pin.off()

    # Wait for the echo pin to go HIGH
    while not echo_pin.value():
        pass

    # Measure the duration of the echo pin being HIGH
    start_time = utime.ticks_us()
    while echo_pin.value():
        pass
    end_time = utime.ticks_us()

    # Calculate the distance in centimeters
    duration = end_time - start_time
    distance = duration / 58

    return distance

def move_forward():
    M1A.duty_u16(0)
    M1B.duty_u16(20000)
    M2A.duty_u16(0)
    M2B.duty_u16(20000)

def stop_motors():
    M1A.duty_u16(0)
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(0)

try:
    while True:
        distance = measure_distance()
        print("Distance: {:.2f} cm".format(distance))

        if distance <= 10:  # If obstacle is within 10cm
            print("Obstacle detected! Stop!")
            stop_motors()
            # You can control the motor movements to achieve the turn.

        else:
            move_forward()

        utime.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram stopped.")

