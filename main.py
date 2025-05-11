from machine import Pin
from servo import Servo
import time

# Initialize PIR sensor on GPIO 0
pir = Pin(19, Pin.IN, Pin.PULL_DOWN)
servo = Servo(pin_id=21) # Initializing Servo on GPIO 21
pir_state = False # Start assuming no motion

print("Proximity Sensor Initialized")
time.sleep(2) # Allow sensor to stabilize
print("Ready")

while True:
    val = pir.value() # Read input value from PIR sensor
    current_time = time.time()
    print(val)
    
    if val == 1: # No proximity detected
        if not pir_state:
            pir_state = True
            servo.write(93.5) # Stop servo
    
    elif val == 0: # Proximity detected
        if pir_state:
            pir_state = False
            servo.write(70) # Move servo
            time.sleep(10) # Food dosage
            
    time.sleep(0.5) # Small delay to prevent spamming
