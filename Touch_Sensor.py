import machine
import time

# Define pins for touch sensor and buzzer
TOUCH_PIN = 4
BUZZER_PIN = 22

# Initialize touch sensor pin as input and buzzer pin as output
touch_pin = machine.Pin(TOUCH_PIN, machine.Pin.IN)
buzzer_pin = machine.Pin(BUZZER_PIN, machine.Pin.OUT)

# Define a function to play a tone on the buzzer for a certain duration
def play_tone(frequency, duration):
    buzzer = machine.PWM(buzzer_pin)
    buzzer.freq(frequency)
    buzzer.duty_u16(32767)  # 50% duty cycle
    time.sleep(duration)
    buzzer.duty_u16(0)
    buzzer.deinit()

# Continuously check the state of the touch sensor and trigger a sound if touched
while True:
    if touch_pin.value() == 1:  # Touch sensor is touched
        play_tone(1000, 0.5)  # Play a 1kHz tone for 0.5 seconds
        time.sleep(0.5)  # Wait for 0.5 seconds before checking again
    else:
        time.sleep(0.1)  # Wait for 0.1 seconds before checking again
