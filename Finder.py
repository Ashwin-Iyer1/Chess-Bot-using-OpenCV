from pynput.mouse import Listener
import logging
import numpy as np
import pyautogui

click_count = 0
positions = np.empty((0, 2), dtype=int)  # Initialize positions as an empty array of shape (0, 2) with integer dtype
def on_click(x, y, button, pressed):
    global click_count, positions
    if pressed:
        click_count += 1
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        temparray = np.array([[x, y]])  # Ensure temparray is shaped as (1, 2)
        positions = np.append(positions, temparray, axis=0)  # Append temparray as a row to positions
        if click_count >= 2:
            # Stop the listener
            return False
def get_region():
    # Start the listener
    with Listener(on_click=on_click) as listener:
        listener.join()


    # Finding the top-left corner
    top_left_corner = np.min(positions, axis=0)

    # Calculating distances of each point from the top-left corner
    distances = np.sum((positions - top_left_corner) ** 2, axis=1)

    # Sorting based on distances
    sorted_indices = np.argsort(distances)
    sorted_positions = positions[sorted_indices]


    print("Top-left corner: ", sorted_positions[0])
    print("Bottom-right corner: ", sorted_positions[1])

    print("width " + str(sorted_positions[1][0] - sorted_positions[0][0]))
    print("height " + str(sorted_positions[1][1] - sorted_positions[0][1]))

    screenshot = pyautogui.screenshot(region=(sorted_positions[0][0], sorted_positions[0][1], sorted_positions[1][0] - sorted_positions[0][0], sorted_positions[1][1] - sorted_positions[0][1]))
    screenshot.save("screenshot.png")
    return sorted_positions[0][0], sorted_positions[0][1], sorted_positions[1][0] - sorted_positions[0][0], sorted_positions[1][1] - sorted_positions[0][1]


