from machine import Pin, PWM
import utime

# Define the Grove servo motor pins
servo1_pin = Pin(0)
servo2_pin = Pin(1)
servo3_pin = Pin(2)
servo4_pin = Pin(3)
servo5_pin = Pin(4)
servo6_pin = Pin(5)

# Create PWM objects for each servo motor
servo1_pwm = PWM(servo1_pin, freq=50)
servo2_pwm = PWM(servo2_pin, freq=50)
servo3_pwm = PWM(servo3_pin, freq=50)
servo4_pwm = PWM(servo4_pin, freq=50)
servo5_pwm = PWM(servo5_pin, freq=50)
servo6_pwm = PWM(servo6_pin, freq=50)

# Define the minimum and maximum pulse widths for each servo
SERVO_MIN_PW = 500 # 0 degree
SERVO_MAX_PW = 2500 # 180 degree

# Function to set the angle of a servo motor
def set_servo_angle(servo_pwm, angle):
    angle = max(0, min(angle, 180)) # Limit the angle to 0-180 degrees
    pw = int((angle / 180) * (SERVO_MAX_PW - SERVO_MIN_PW) + SERVO_MIN_PW) # Calculate the pulse width
    servo_pwm.duty_ns(pw * 1000) # Set the pulse width in nanoseconds

# Spider walk pattern
spider_walk_pattern = [
    [90, 90, 90, 90, 90, 90],
    [130, 50, 130, 50, 130, 50],
    [50, 130, 50, 130, 50, 130],
    [90, 90, 90, 90, 90, 90]
]

# Function to perform the spider walk pattern
def spider_walk():
    for i in range(len(spider_walk_pattern)):
        for j in range(6):
            set_servo_angle(servo1_pwm, spider_walk_pattern[i][0])
            set_servo_angle(servo2_pwm, spider_walk_pattern[i][1])
            set_servo_angle(servo3_pwm, spider_walk_pattern[i][2])
            set_servo_angle(servo4_pwm, spider_walk_pattern[i][3])
            set_servo_angle(servo5_pwm, spider_walk_pattern[i][4])
            set_servo_angle(servo6_pwm, spider_walk_pattern[i][5])
            utime.sleep_ms(50)

# Perform the spider walk pattern indefinitely
while True:
    spider_walk()

    
#This code defines 6 Grove servo motor pins and creates PWM objects for each motor. It also defines the minimum and maximum pulse widths for each servo motor, and a function to set the angle of a servo motor based on a given PWM object and angle.
#The spider walk pattern is defined as a list of lists, where each inner list represents the angles for each servo motor at a given step in the pattern. The spider_walk() function loops through the steps in the pattern and sets the angle of each servo motor using the set_servo_angle() function. The function then sleeps for 50 milliseconds before moving to the next step in the pattern.
#The code then enters an infinite loop and repeatedly performs the spider walk pattern using the spider_walk() function.
