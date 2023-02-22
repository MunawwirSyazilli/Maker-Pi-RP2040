import machine
import utime

# Configure Ultrasonic Sensor
trigger = machine.Pin(0, machine.Pin.OUT)
echo = machine.Pin(1, machine.Pin.IN)

# Configure Servo Motor
servo = machine.PWM(machine.Pin(2))
servo.freq(50)

# Configure TT Motor
ena = machine.Pin(3, machine.Pin.OUT)
in1 = machine.Pin(4, machine.Pin.OUT)
in2 = machine.Pin(5, machine.Pin.OUT)
enb = machine.Pin(6, machine.Pin.OUT)
in3 = machine.Pin(7, machine.Pin.OUT)
in4 = machine.Pin(8, machine.Pin.OUT)

# Configure Infrared Sensor
ir = machine.Pin(9, machine.Pin.IN)

# Configure Touch Sensor
touch = machine.Pin(10, machine.Pin.IN)

# Set TT Motor Speed
speed = 50

def ultrasonic_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

def servo_angle(angle):
    duty = 20 + (angle / 180) * 100
    servo.duty_u16(int(duty * 65535 / 100))

def forward():
    ena.value(1)
    in1.value(1)
    in2.value(0)
    enb.value(1)
    in3.value(1)
    in4.value(0)

def stop():
    ena.value(0)
    in1.value(0)
    in2.value(0)
    enb.value(0)
    in3.value(0)
    in4.value(0)

while True:
    distance = ultrasonic_distance()
    
    if distance > 30:
        servo_angle(90)
        forward()
    elif distance <= 30:
        servo_angle(60)
        if ir.value() == 0:
            servo_angle(120)
            ena.value(0)
            enb.value(0)
            utime.sleep(1)
        else:
            forward()
    
    if touch.value() == 1:
        stop()
        break
