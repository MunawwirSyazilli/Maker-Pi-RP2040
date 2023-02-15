import machine
import time

servo_pin = machine.Pin(12)
pwm = machine.PWM(servo_pin)
pwm.freq(50)
def move_servo(angle):
    duty_cycle = angle / 18 + 2
    pwm.duty_u16(int(duty_cycle * 65535 / 100))
while True:
    move_servo(0) # Move the servo motor to 0 degrees
    time.sleep(1)
    move_servo(90) # Move the servo motor to 90 degrees
    time.sleep(1)
    move_servo(180) # Move the servo motor to 180 degrees
    time.sleep(1)
