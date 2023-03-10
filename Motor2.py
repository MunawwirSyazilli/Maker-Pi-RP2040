import machine
import utime

# Define pins for motor control
MOTOR_LEFT_PIN1 = 8
MOTOR_LEFT_PIN2 = 9
MOTOR_RIGHT_PIN1 = 10
MOTOR_RIGHT_PIN2 = 11

# Define pins for ultrasonic sensor
ULTRASONIC_TRIGGER_PIN = 2
ULTRASONIC_ECHO_PIN = 3

# Initialize motor control pins as output pins
motor_left_pin1 = machine.Pin(MOTOR_LEFT_PIN1, machine.Pin.OUT)
motor_left_pin2 = machine.Pin(MOTOR_LEFT_PIN2, machine.Pin.OUT)
motor_right_pin1 = machine.Pin(MOTOR_RIGHT_PIN1, machine.Pin.OUT)
motor_right_pin2 = machine.Pin(MOTOR_RIGHT_PIN2, machine.Pin.OUT)

# Initialize ultrasonic sensor pins
ultrasonic_trigger_pin = machine.Pin(ULTRASONIC_TRIGGER_PIN, machine.Pin.OUT)
ultrasonic_echo_pin = machine.Pin(ULTRASONIC_ECHO_PIN, machine.Pin.IN)

# Function to measure distance using ultrasonic sensor
def measure_distance():
    # Send a 10us pulse to trigger the ultrasonic sensor
    ultrasonic_trigger_pin.on()
    utime.sleep_us(10)
    ultrasonic_trigger_pin.off()
    
    # Wait for the echo pin to go high and then low
    while not ultrasonic_echo_pin.value():
        pass
    start_time = utime.ticks_us()
    while ultrasonic_echo_pin.value():
        pass
    end_time = utime.ticks_us()
    
    # Calculate distance in cm
    duration = utime.ticks_diff(end_time, start_time)
    distance = duration / 58
    
    return distance

# Move forward continuously until an object is detected in a certain distance
while True:
    distance = measure_distance()
    
    if distance < 20:  # Stop if object is within 20cm
        motor_left_pin1.off()
        motor_left_pin2.off()
        motor_right_pin1.off()
        motor_right_pin2.off()
    else:
        motor_left_pin1.on()
        motor_left_pin2.off()
        motor_right_pin1.on()
        motor_right_pin2.off()
        
    utime.sleep(1)

