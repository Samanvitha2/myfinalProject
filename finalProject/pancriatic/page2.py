import tkinter as tk
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import filedialog, messagebox
from tkinter import filedialog, messagebox
#from ultralytics import YOLO
import os, shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import ImageTk, Image
#import cv2


from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
class Page2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.background_image = tk.PhotoImage(file="bg.png")  # Replace with your image path
        # Create a label to display the background image
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def stagetest():
            os.system("python GUI_test.py")


        def sampleBasedTest():
            os.system("python afterstagetesting.py")

        # Upload Image Button
        upload = Button(self, text="Stage Test", command=stagetest, padx=15, pady=10)
        upload.configure(background='#5E81AC', foreground='white', font=('Helvetica', 14, 'bold'), relief="flat",
                         borderwidth=0)  # Same color for consistency
        upload.grid(row=3, column=0, padx=20, pady=10)  # First button, side by side in row 7

        # Classify Image Button
        classify_button = Button(self, text="sample Based Prediction", command=sampleBasedTest, padx=15, pady=10)
        classify_button.configure(background='#5E81AC', foreground='white', font=('Helvetica', 14, 'bold'),
                                  relief="flat", borderwidth=0)  # Same color for consistency
        classify_button.grid(row=3, column=1, padx=20, pady=10)  # Second button, side by side in row 7

        # Heading with clean, large font
        heading = Label(self, text="Pancriatics disease detection", pady=20, font=('Helvetica', 30, 'bold'))
        heading.configure(background='#F0F0F0', foreground='#2E3440')  # Dark gray heading for contrast
        heading.grid(row=0, column=0, columnspan=2)

        # Center the layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)

