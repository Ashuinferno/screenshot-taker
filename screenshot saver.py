from tkinter import mainloop
import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def take_screenshot():
    my_screenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    my_screenshot.save(save_path + "_screenshot.png")

myButton = tk.Button(text="Take Screenshot", command=take_screenshot)
canvas1.create_window(150, 150, window=myButton)

mainloop()
