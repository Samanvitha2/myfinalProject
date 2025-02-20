import tkinter as tk
from PIL import ImageTk, Image
class Page5(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.background_image = tk.PhotoImage(file="bg.png")  # Replace with your image path
        # Create a label to display the background image
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title label
        title = tk.Label(self, text="Contact Us", font=("Arial", 24), bg="white")
        title.pack(pady=10)

        # Contact Information Labels
        address_label = tk.Label(self, text="Address:", font=("Arial", 14, "bold"), bg="white")
        address_label.pack(anchor="w", padx=20)

        address_content = tk.Label(self, text="1234 Main Street\nCityville, Country 56789",
                                   font=("Arial", 12), bg="white", justify="left")
        address_content.pack(anchor="w", padx=40, pady=5)

        phone_label = tk.Label(self, text="Phone:", font=("Arial", 14, "bold"), bg="white")
        phone_label.pack(anchor="w", padx=20)

        phone_content = tk.Label(self, text="+91 6361715130", font=("Arial", 12), bg="white")
        phone_content.pack(anchor="w", padx=40, pady=5)

        email_label = tk.Label(self, text="Email:", font=("Arial", 14, "bold"), bg="white")
        email_label.pack(anchor="w", padx=20)

        email_content = tk.Label(self, text="samanvitha2002@gmail.com", font=("Arial", 12), bg="white")
        email_content.pack(anchor="w", padx=40, pady=5)

        # Message section
        message = tk.Label(self, text="PES institute of technology!\n"
                                      "Shimoga.", font=("Arial", 12),
                           bg="white", wraplength=400, justify="left")
        message.pack(pady=20, padx=20)

        try:
            # Open the image file and resize it
            image = Image.open("5.png")  # Replace with your image path
            image = image.resize((250, 150), Image.LANCZOS)
            image_tk = ImageTk.PhotoImage(image)

            # Create a label to display the image
            image_label = tk.Label(self, image=image_tk, bg="white")
            image_label.image = image_tk  # Keep a reference to avoid garbage collection
            image_label.pack(pady=10)
        except Exception as e:
            error_label = tk.Label(self, text="Image could not be loaded.", font=("Arial", 12), bg="white", fg="red")
            error_label.pack(pady=10)
            print(f"Error loading image: {e}")

