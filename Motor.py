from machine import Pin

motor1_pin1 = Pin(8, Pin.OUT)
motor1_pin2 = Pin(9, Pin.OUT)
motor2_pin1 = Pin(10, Pin.OUT)
motor2_pin2 = Pin(11, Pin.OUT)

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
    motor1_pin1.duty(speed * 10)
    motor1_pin2.duty(speed * 10)
    motor2_pin1.duty(speed * 10)
    motor2_pin2.duty(speed * 10)

control_motor(50, "forward") # Move the TT motor forward at 50% speed

