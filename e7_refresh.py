import tkinter as tk
import pyautogui
import time
from pynput import keyboard

# resulution:1920x1080
# windowed mode Pc client

def get_screen_resolution():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return width, height

def left_click_at(x, y):
    #pyautogui.click(x=x, y=y)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()

def move_mouse_to(x, y):
    pyautogui.moveTo(x, y)

def double_click_at(x, y):
    pyautogui.click(x=x, y=y, clicks=2, interval=0.25)

def print_mouse_position():
    x, y = pyautogui.position()
    print(f"Current mouse position: ({x}, {y})")

def scroll_down(amount=1000):
    pyautogui.scroll(-amount)

def refresh():
    time.sleep(1)
    # Click the refresh button
    left_click_at(447, 955)
    time.sleep(2)
    # Click the confirm refresh button
    left_click_at(1114, 672)
    time.sleep(1)
    # Move the mouse to the top of the list
    move_mouse_to(1285, 227)
    time.sleep(1)
    # Scroll to the top of the list
    #scroll_down(1000)
    #time.sleep(1)

def print_pixel_color_at_mouse():
    x, y = pyautogui.position()
    screenshot = pyautogui.screenshot()
    color = screenshot.getpixel((x, y))
    print(f"Color of pixel at ({x}, {y}): {color}")

def is_pixel_color(x, y, expected_color):
    screenshot = pyautogui.screenshot()
    actual_color = screenshot.getpixel((x, y))
    return actual_color == expected_color

def check_bm_1_to_4():
    # row 1
    if is_pixel_color(894, 199, (177, 91, 33)):
        print("BM found at (894, 199)")
        return [1696, 249]
    if is_pixel_color(894, 199, (250, 65, 22)):
        print("Mystic found at (894, 199)")
        return [1696, 249]
    # row 2
    if is_pixel_color(895, 403, (174, 86, 30)):
        print("BM found at (895, 403)")
        return [1696, 460]
    if is_pixel_color(895, 403, (250, 65, 22)):
        print("Mystic found at (895, 403)")
        return [1696, 460]
    # row 3
    if is_pixel_color(895, 609, (178, 93, 34)):
        print("BM found at (895, 609)")
        return [1696, 666]
    if is_pixel_color(895, 609, (250, 65, 22)):
        print("Mystic found at (895, 609)")
        return [1696, 666]
    # row 4
    if is_pixel_color(895, 816, (179, 95, 36)):
        print("BM found at (895, 816)")
        return [1696, 870]
    if is_pixel_color(895, 816, (250, 61, 21)):
        print("Mystic found at (895, 816)")
        return [1696, 870]
    else:
        print("No BMs or Mystics found in rows 1 to 4")
        return False
    
def check_bm_5_to_6():    
    # row 5
    if is_pixel_color(893, 714, (180, 100, 40)):
        print("BM found at (893, 714)")
        return [1696, 770]
    if is_pixel_color(893, 714, (250, 65, 22)):
        print("Mystic found at (893, 714)")
        return [1696, 770]
    # row 6
    if is_pixel_color(893, 920, (181, 103, 42)):
        print("BM found at (893, 920)")
        return [1696, 970]
    if is_pixel_color(893, 920, (252, 62, 21)):
        print("Mystic found at (893, 920)")
        return [1696, 970]
    else:
        print("No BMs or Mystics found in rows 5 to 6")
        return False
    
def buy(item):
    if item:
        x, y = item
        # Click the buy button
        left_click_at(x, y)
        time.sleep(1)
        # Click the confirm buy button
        left_click_at(1150, 743)
        time.sleep(1)
    else:
        print("No items to buy")

def refresh_loop():

    stop_loop = False

    def on_press(key):
        nonlocal stop_loop
        if key == keyboard.Key.esc:
            stop_loop = True
            return False  # Stop the listener

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while not stop_loop:
        time.sleep(1)

        # Check for BMs and Mystics in rows 1 to 4
        if check_bm_1_to_4():
            print("BM or Mystic found in rows 1 to 4")
            buy(check_bm_1_to_4())
            #break

        time.sleep(1)
        scroll_down(1000)
        time.sleep(1)

        # Check for BMs and Mystics in rows 5 to 6
        if check_bm_5_to_6():
            print("BM or Mystic found in rows 5 to 6")
            buy(check_bm_5_to_6())
            #break

        else:
            # Refresh and move to the top of the list
            refresh()

    listener.stop()
    print("Refresh loop stopped by user.")

def auto_buy(check_condition):
    while check_condition():
        # Refresh and move to the top of the list
        refresh()

        # Coordinates and expected colors for BMs and Mystics
        items = [
            {"coords": (894, 199), "bm_color": (177, 91, 33), "mystic_color": (250, 65, 22), "buy_btn": (1696, 249)},
            {"coords": (895, 403), "bm_color": (174, 86, 30), "mystic_color": (250, 65, 22), "buy_btn": (1696, 460)},
            {"coords": (895, 609), "bm_color": (178, 93, 34), "mystic_color": (250, 65, 22), "buy_btn": (1696, 666)},
            {"coords": (895, 816), "bm_color": (179, 95, 36), "mystic_color": (250, 61, 21), "buy_btn": (1696, 870)},
            {"coords": (893, 714), "bm_color": (180, 100, 40), "mystic_color": (250, 65, 22), "buy_btn": (1696, 770)},
            {"coords": (893, 920), "bm_color": (181, 103, 42), "mystic_color": (252, 62, 21), "buy_btn": (1696, 970)},
        ]

        for item in items:
            x, y = item["coords"]
            bm_color = item["bm_color"]
            mystic_color = item["mystic_color"]
            buy_btn = item["buy_btn"]

            # Check for BM color
            if is_pixel_color(x, y, bm_color):
                print(f"BM found at ({x}, {y}), buying...")
                left_click_at(*buy_btn)
                time.sleep(1)

            # Check for Mystic color
            elif is_pixel_color(x, y, mystic_color):
                print(f"Mystic found at ({x}, {y}), buying...")
                left_click_at(*buy_btn)
                time.sleep(1)

if __name__ == "__main__":
    time.sleep(2)
    screen_width, screen_height = get_screen_resolution()
    print(f"Screen resolution: {screen_width}x{screen_height}")

    refresh_loop()
    #print_mouse_position()
    #refresh()
    #print_pixel_color_at_mouse()

    #screenshot = pyautogui.screenshot()
    #actual_color = screenshot.getpixel((893, 920))
    #print(actual_color)

    #print(is_pixel_color(893, 920, (252, 62, 21)))



# refrsh btn -> (447,955)
# confirm refresh btn -> (1114, 672)
# top of the list -> (1285, 227)
# buy confirm btn -> (1150, 743)

# Row | Coordinates | BMs            | Mystics       | Buy btn
# 1   | (894, 199)  | (177, 91, 33)  | (250, 65, 22) | (1696, 249)
# 2   | (895, 403)  | (174, 86, 30)  | (250, 65, 22) | (1696, 460)
# 3   | (895, 609)  | (178, 93, 34)  | (250, 65, 22) | (1696, 666)
# 4   | (895, 816)  | (179, 95, 36)  | (250, 61, 21) | (1696, 870)
# 5   | (893, 714)  | (180, 100, 40) | (250, 65, 22) | (1696, 770)
# 6   | (893, 920)  | (181, 103, 42) | (252, 62, 21) | (1696, 970)
