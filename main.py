import glob
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tkinter as tk

images = []
labels = []

#index = 0
"""
def class1_label():
    labels.append("Chess")
    print(labels)
    next_img()

def class2_label():
    labels.append("Not Chess")
    print(labels)
    next_img()

def next_img():
    print("Next img")
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    img = tk.PhotoImage(file='images\image2.png')
    canvas.create_image(20, 20, image=img)
    tk.mainloop()

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

images.extend(glob.glob('images/*.png'))

img = tk.PhotoImage(file=images[0])
canvas.create_image(20, 20, 20, 20 image=img)

class1_button = tk.Button()
class1_button["text"] = "Chess"
class1_button["command"] = class1_label
class1_button.pack()

class2_button = tk.Button()
class2_button["text"] = "Not Chess"
class2_button["command"] = class2_label
class2_button.pack()

tk.mainloop()
"""

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.labels = []
        self.img = tk.PhotoImage(file='images\image2.png')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()
        self.canvas.create_image(20, 20, image=self.img)
        self.canvas.image = self.img;

        self.class1_button = tk.Button()
        self.class1_button["text"] = "Chess"
        self.class1_button["command"] = self.class1_label
        self.class1_button.pack()

        self.class2_button = tk.Button()
        self.class2_button["text"] = "Not Chess"
        self.class2_button["command"] = self.class2_label
        self.class2_button.pack()

    def class1_label():
        labels.append("Chess")
        next_img()

    def class2_label():
        labels.append("Not Chess")
        print(labels)

root = tk.Tk()
app = App(master=root)
app.mainloop()
