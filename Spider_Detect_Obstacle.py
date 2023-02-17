from machine import Pin, PWM
import utime
import grove_i2c_motor_driver
import hcsr04

# Initialize the Grove motor driver and ultrasonic sensor
md = grove_i2c_motor_driver.Driver()
ultrasonic = hcsr04.HCSR04(trigger_pin=17, echo_pin=16)

# Initialize the PWM pins for the servo motors
servo_pins = [12, 13, 14, 15, 18, 19]
servos = []
for pin in servo_pins:
    pwm = PWM(Pin(pin))
    pwm.freq(50)
    servos.append(pwm)

# Define the servo angles for different spider movements
forward_angles = [30, 150, 90, 90, 150, 30]
left_angles = [10, 140, 90, 90, 140, 10]
right_angles = [50, 170, 90, 90, 170, 50]
backward_angles = [150, 30, 90, 90, 30, 150]

# Set the initial direction and speed of the spider
direction = "forward"
speed = 100

# Define a function to set the angles of the servo motors
def set_servo_angles(angles):
    for i in range(len(angles)):
        duty = angles[i] * 65535 // 200 + 32768
        servos[i].duty_u16(duty)

# Define a function to control the spider movement
def control_spider():
    # Check the distance to an object in front
    distance = ultrasonic.distance_cm()
    if distance < 10: # If an object is too close, change direction
        if direction == "forward":
            direction = "backward"
        elif direction == "backward":
            direction = "forward"
        elif direction == "left":
            direction = "right"
        elif direction == "right":
            direction = "left"
        # Wait a bit before changing direction again
        utime.sleep(1)
    # Set the angles of the servo motors based on the current direction
    if direction == "forward":
        set_servo_angles(forward_angles)
        md.set_motor_speed(1, speed)
        md.set_motor_speed(2, speed)
    elif direction == "backward":
        set_servo_angles(backward_angles)
        md.set_motor_speed(1, -speed)
        md.set_motor_speed(2, -speed)
    elif direction == "left":
        set_servo_angles(left_angles)
        md.set_motor_speed(1, -speed)
        md.set_motor_speed(2, speed)
    elif direction == "right":
        set_servo_angles(right_angles)
        md.set_motor_speed(1, speed)
        md.set_motor_speed(2, -speed)

# Move the spider continuously
while True:
    control_spider()

    
    
#Note that this code is just an example and may need to be adjusted based on the specific servo motors and ultrasonic sensor used.
