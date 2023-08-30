import pyautogui
from time import sleep

"""
Important Note!
AutoPyGui comes with a built-in failsafe in case something goes wrong with a command.
To stop script, move mouse to any corner of the screen.
"""

long_pause = 0.28  # Some page functions take a second (or a quarter) to load in

for _ in range(10):  # Repeat for _ tickets
    match = pyautogui.locateOnScreen('./add_tag.JPG', confidence=0.8)  # Locate topmost "add tag" field
    match_centered = pyautogui.center(match)  # Locate center of "add tag" field
    pyautogui.moveTo(match_centered[0], match_centered[1])  # Move cursor to "add tag" field
    pyautogui.click()
    pyautogui.write("RM is Keeping Asset")  # Enter tag text
    sleep(long_pause)  # Wait for drop-down suggestions to load in
    pyautogui.press('down')  # Select drop-down suggestion for tag
    pyautogui.hotkey('enter')  # Hit enter to submit tag
    sleep(long_pause)  # Wait to ensure field is properly populated
    for _ in range(4):  # Hit tab four times to unselect text field and bring next text fields into view
        pyautogui.hotkey('tab')
    for _ in range(2):  # Scroll down to avoid matching "add tag" area in already-tagged ticket
        pyautogui.press('down')
    sleep(long_pause * 2)  # Give a moment to trigger failsafe if needed (mouse to corner of screen)

profile_circle = pyautogui.locateOnScreen('./profile_circle.JPG', confidence=0.8)
pyautogui.moveTo(profile_circle)  # At the end of the loop, move mouse to corner to show finished
print("Round finished!")
