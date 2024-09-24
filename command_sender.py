import time

def send_command():
    while True:
        command = input("Enter command (obstacle, obstacle removed, obstacle ca>
        with open('command.txt', 'w') as file:
            file.write(command)
        if command == 'exit':
            break
        time.sleep(0.1)  # Small delay to allow the file to be properly updated

if __name__ == "__main__":
    send_command()
