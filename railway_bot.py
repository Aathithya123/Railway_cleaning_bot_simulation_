import time
import os
import requests  


TRIG_LEFT = 5
ECHO_LEFT = 6
TRIG_RIGHT = 13
ECHO_RIGHT = 12

# Your OneSignal credentials
ONESIGNAL_APP_ID = '________________________________________'
ONESIGNAL_API_KEY = '_______________________________________'

def send_notification(message):
    url = 'https://onesignal.com/api/v1/notifications'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Basic {ONESIGNAL_API_KEY}'
    }
    data = {
        'app_id': ONESIGNAL_APP_ID,
        'contents': {'en': message},
        'included_segments': ['All']  
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f'Notification sent successfully: {message}')
    else:
        print(f'Failed to send notification: {response.status_code}, {response.text}')

class MockMotor:
    def _init_(self, forward=None, backward=None):
        self.forward_pin = forward
        self.backward_pin = backward
    
    def forward(self):
        pass
    
    def backward(self):
        if self.backward_pin:
            print(f"Motor Backward: {self.backward_pin}")
        else:
            print("Motor cannot go backward")

    def stop(self):
        print(f"Motor Stopped: {self.forward_pin}, {self.backward_pin}")

class MockServo:
    def _init_(self, pin):
        self.pin = pin

    def set_angle(self, angle):
        print(f"Servo {self.pin} set to angle {angle}")

def measure_distance(trig, echo):
    print(f"Measuring distance with TRIG {trig} and ECHO {echo}")
    return 25  

def clean_with_servo(servo):
    servo.set_angle(90)  
    time.sleep(1)
    servo.set_angle(0)  

def read_command():
    try:
        with open('command.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def clean_track(duration):
    motors = {
        'left_front': MockMotor(forward=17, backward=18),
        'left_rear': MockMotor(forward=22, backward=23),
        'right_front': MockMotor(forward=24, backward=25),
        'right_rear': MockMotor(forward=26, backward=27)
    }
    cleaning_motors = {
        'cleaning_left': MockMotor(forward=19),
        'cleaning_right': MockMotor(forward=20)
    }
    servos = {
        'left': MockServo(pin=21),
        'right': MockServo(pin=16)
    }

   
    for name, motor in motors.items():
        print(f"Motor {name} started")
        motor.forward()
    for name, motor in cleaning_motors.items():
        print(f"Motor {name} started")
        motor.forward()

    start_time = time.time()

    obstacle_detected = False
    obstacle_removed = False
    notification_sent = False  

    while time.time() - start_time < duration:
        distance_left = measure_distance(TRIG_LEFT, ECHO_LEFT)
        distance_right = measure_distance(TRIG_RIGHT, ECHO_RIGHT)

        command = read_command()
        if command == 'obstacle':
            if not obstacle_detected:
                print("Obstacle detected, stopping motors and activating cleaning...")
                obstacle_detected = True
            for motor in motors.values():
                motor.stop()
            for motor in cleaning_motors.values():
                motor.forward()  
            for servo in servos.values():
                clean_with_servo(servo)
        elif command == 'obstacle removed':
            if not obstacle_removed:
                print("Obstacle removed, resuming normal operation...")
                obstacle_removed = True
            for motor in motors.values():
                motor.forward()
            for motor in cleaning_motors.values():
                motor.forward()
        elif command == 'obstacle cannot be removed':
            if not notification_sent:  
                print("Obstacle cannot be removed, sending notification and stopping all motors...")
                send_notification("Obstacle cannot be removed")
                notification_sent = True  
            for motor in motors.values():
                motor.stop()
            for motor in cleaning_motors.values():
                motor.stop()
        elif command == 'exit':
            print("Exit command received, stopping the bot...")
            break

        time.sleep(0.1)

    for name, motor in motors.items():
        print(f"Motor {name} stopped")
        motor.stop()
    for name, motor in cleaning_motors.items():
        print(f"Motor {name} stopped")
        motor.stop()

try:
    clean_track(60)

except KeyboardInterrupt:
    print("Stopping the bot due to KeyboardInterrupt.")

finally:
    print("Cleanup done.")
    if os.path.exists('command.txt'):
        os.remove('command.txt')
