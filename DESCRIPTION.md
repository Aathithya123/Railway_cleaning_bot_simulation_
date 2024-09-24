# Railway_cleaning_bot_simulation_
This railway track cleaning bot uses four DC motors for movement and two for cleaning the inside of the track. Ultrasonic sensors detect obstacles, and servo motors with brushes clear them. The bot sends notifications via OneSignal if an obstacle can't be cleared and stops until resolved. It simulates real-time operation using Python scripts.

Project Components:
Four DC Motors (for movement): These motors control the movement of the bot along the railway track. When the bot is powered on, these motors are activated, and the bot begins moving.

Two DC Motors (for track cleaning): Located at the bottom of the bot, these motors are always on, cleaning the inside of the railway track while the bot moves.

Ultrasonic Sensors (for obstacle detection): Two ultrasonic sensors are mounted above the front wheels, one on each side of the bot. These sensors continuously sense the track for any obstacles in front of the bot.

Servo Motors (for obstacle cleaning): Each ultrasonic sensor is connected to a servo motor with a cleaning brush at its end. If an obstacle is detected, the corresponding servo motor is activated, moving the brush to clean the track and remove the obstacle.

Bot Operation:
Initial Movement: When powered on, the bot's four DC motors start moving the bot forward along the track, while the two cleaning motors continuously clean the inside of the track.

Obstacle Detection and Cleaning:

The ultrasonic sensors detect any obstacles in the bot's path.
If an obstacle is detected, the bot's movement motors stop, and the corresponding servo motor activates to clean the track by brushing the obstacle away.
After the obstacle is removed, the bot resumes its normal operation.
Command-based Simulation:

A separate script, command_sender.py, allows manual simulation of various events (e.g., obstacle detection, obstacle removal).
Commands such as "obstacle," "obstacle removed," and "obstacle cannot be removed" can be typed in the command sender to simulate the corresponding actions of the bot.
Notification System:

If the bot detects an obstacle that cannot be removed, a notification is sent to the user via OneSignal, alerting them that the obstacle must be manually cleared.
The bot will stop all motors until the obstacle is addressed.
Track Distance Completion:

The bot is programmed to clean a given section of track. After completing the specified track distance, the bot will stop, indicating the cleaning is complete.
Code Structure:
railway_bot.py:
Simulates the main logic of the bot, including motor control, obstacle detection, and the servo-based cleaning mechanism.
Integrates with OneSignal API to send notifications when the bot encounters an obstacle that cannot be removed.
command_sender.py:
Allows users to input commands like "obstacle" or "obstacle removed," simulating various states of the bot.
Commands are written to a text file that railway_bot.py reads and responds to.


This project is designed to mimic the real-world behavior of a railway track cleaning system, providing an interactive way to demonstrate automated cleaning and obstacle handling. The bot is capable of operating autonomously with minimal user intervention, enhancing the efficiency and safety of railway track maintenance.
