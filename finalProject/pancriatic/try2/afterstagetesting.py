import tkinter as tk
from tkinter import messagebox

import pandas as pd
import joblib
import numpy as np

# Load the trained model and preprocessing components


model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
y_encoder = joblib.load('label_encoder.pkl')

def predict():

    try:
        # Get user inputs
        plasma_CA19_9 = float(entry_plasma_CA19_9.get())
        creatinine = float(entry_creatinine.get())
        LYVE1 = float(entry_LYVE1.get())
        REG1B = float(entry_REG1B.get())
        TFF1 = float(entry_TFF1.get())
        REG1A = float(entry_REG1A.get())

        # Prepare the input array as a DataFrame with feature names
        input_data = pd.DataFrame(
            [[plasma_CA19_9, creatinine, LYVE1, REG1B, TFF1, REG1A]],
            columns=['plasma_CA19_9', 'creatinine', 'LYVE1', 'REG1B', 'TFF1', 'REG1A']
        )

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Predict using the model
        prediction = model.predict(input_data_scaled)

        # Decode the prediction
        diagnosis = y_encoder.inverse_transform(prediction)[0]

        # Show the result
        messagebox.showinfo("Prediction Result", f"Predicted Diagnosis: {diagnosis}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the GUI window
root = tk.Tk()
root.title("Diagnosis Predictor")

# Input labels and entry fields
labels = ["Plasma CA19-9:", "Creatinine:", "LYVE1:", "REG1B:", "TFF1:", "REG1A:"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_plasma_CA19_9 = entries[0]
entry_creatinine = entries[1]
entry_LYVE1 = entries[2]
entry_REG1B = entries[3]
entry_TFF1 = entries[4]
entry_REG1A = entries[5]

# Predict button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
