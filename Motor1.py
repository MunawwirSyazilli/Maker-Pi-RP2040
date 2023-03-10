import machine
import utime

# Define pins for motor control
MOTOR_LEFT_PIN1 = 8
MOTOR_LEFT_PIN2 = 9
MOTOR_RIGHT_PIN1 = 10
MOTOR_RIGHT_PIN2 = 11

# Initialize motor control pins as output pins
motor_left_pin1 = machine.Pin(MOTOR_LEFT_PIN1, machine.Pin.OUT)
motor_left_pin2 = machine.Pin(MOTOR_LEFT_PIN2, machine.Pin.OUT)
motor_right_pin1 = machine.Pin(MOTOR_RIGHT_PIN1, machine.Pin.OUT)
motor_right_pin2 = machine.Pin(MOTOR_RIGHT_PIN2, machine.Pin.OUT)

# Move forward continuously
while True:
    motor_left_pin1.on()
    motor_left_pin2.off()
    motor_right_pin1.on()
    motor_right_pin2.off()
    utime.sleep(1)
