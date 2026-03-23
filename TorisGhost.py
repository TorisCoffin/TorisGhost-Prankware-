import pyautogui
import random
import time
import tkinter as tk
import threading
from tkinter import messagebox

def spawn_random_window(main_root, title, message):
   
   window = tk.Toplevel(main_root)
   window.title(title)

   screen_width = window.winfo_screenwidth()
   screen_height = window.winfo_screenheight()

   win_w, win_h = 300, 120
   random_x = random.randint(0, screen_width - win_w)
   random_y = random.randint(0, screen_height - win_h)
   
   window.geometry(f"{win_w}x{win_h}+{random_x}+{random_y}")
   window.attributes("-topmost", True)
   
   tk.Label(window, text=message, pady=10).pack()
   tk.Button(window, text="ok", command=window.destroy).pack()

def mouse_shaker():
    while True:
        x,y = pyautogui.position()
        pyautogui.position()
        pyautogui.moveTo(x + random.randint(-100, 100), y + random.randint(-100, 100))
        time.sleep(0.1)

def window_loop(root):
    spawn_random_window(root,"Aviso","FEED ME! T.T")
    root.after(1000, lambda: window_loop(root))

def start_haunting():
    print("Hello! Press Ctrl + C in this terminal to make it stop")

    root = tk.Tk()
    root.withdraw()
    
    t=threading.Thread(target=mouse_shaker, daemon=True)
    t.start()

    window_loop(root)
    root.mainloop()


if __name__ == "__main__":
    start_haunting()