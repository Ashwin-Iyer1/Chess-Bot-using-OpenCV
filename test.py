import keyboard
import pyautogui
from PIL import Image

def create_image():
    # Capture the specified screen region
    screenshot = pyautogui.screenshot(region=(590, 165, 680, 670))

    # Save the captured region as "new_board.jpeg"
    screenshot.save("board.jpg")
    print("Image created")

def on_keypress(event):
    if event.name == 'esc':  # Exit the program if the 'esc' key is pressed
        keyboard.unhook_all()
        print("Exiting the program...")
        exit()
    elif event.name == 'g' and event.event_type == 'down':  # Capture and create the image when 'g' key is pressed
        create_image()

# Register the keypress event listener
keyboard.on_press(on_keypress)

# Start the keyboard event listener
keyboard.wait()
