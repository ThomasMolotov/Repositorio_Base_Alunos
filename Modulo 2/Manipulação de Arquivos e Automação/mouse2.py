import pyautogui, time

for i in range(55):
    x, y = pyautogui.position()
    print(f"pyautogui.dragTo({x}, {y})")
    time.sleep(0.1)