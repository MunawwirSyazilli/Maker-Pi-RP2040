from machine import Pin, PWM
import utime

motor1_pin1 = Pin(8, Pin.OUT)
motor1_pin2 = Pin(9, Pin.OUT)
motor2_pin1 = Pin(10, Pin.OUT)
motor2_pin2 = Pin(11, Pin.OUT)

motor1_pwm1 = PWM(motor1_pin1)
motor1_pwm2 = PWM(motor1_pin2)
motor2_pwm1 = PWM(motor2_pin1)
motor2_pwm2 = PWM(motor2_pin2)

button_pin = Pin(15, Pin.IN, Pin.PULL_UP)

def control_motor(speed, direction):
    if direction == "forward":
        motor1_pin1.on()
        motor1_pin2.off()
        motor2_pin1.on()
        motor2_pin2.off()
    elif direction == "backward":
        motor1_pin1.off()
        motor1_pin2.on()
        motor2_pin1.off()
        motor2_pin2.on()
    elif direction == "right":
        motor1_pin1.off()
        motor1_pin2.on()
        motor2_pin1.on()
        motor2_pin2.off()
    elif direction == "left":
        motor1_pin1.on()
        motor1_pin2.off()
        motor2_pin1.off()
        motor2_pin2.on()
    else:
        motor1_pin1.off()
        motor1_pin2.off()
        motor2_pin1.off()
        motor2_pin2.off()
        
    speed = max(0, min(speed, 100))
    motor1_pwm1.duty_u16(speed * 65535 // 100)
    motor1_pwm2.duty_u16(speed * 65535 // 100)
    motor2_pwm1.duty_u16(speed * 65535 // 100)
    motor2_pwm2.duty_u16(speed * 65535 // 100)

speed = 50
direction = "forward"

while True:
    if button_pin.value() == 0:
        if direction == "forward":
            direction = "backward"
        else:
            direction = "forward"
        utime.sleep_ms(200) # Debounce the button press
    control_motor(speed, direction)
