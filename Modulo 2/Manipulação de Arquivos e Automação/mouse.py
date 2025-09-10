import pyautogui, time

for i in range(100):
    x, y = pyautogui.position()
    print(f"Posição atual do mouse: {x}, {y}")
    time.sleep(0.1)