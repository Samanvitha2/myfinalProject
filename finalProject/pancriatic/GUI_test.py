import pandas as pd
import joblib
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# Load the saved model, encoders, and scaler
model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
scaler = joblib.load('scaler.pkl')

# Create a Tkinter window
window = Tk()
window.title("Diagnosis Prediction")
window.geometry("400x350")

# Input variables
inputs = {
    'sample_id': StringVar(),
    'patient_cohort': StringVar(),
    'sample_origin': StringVar(),
    'age': StringVar(),
    'sex': StringVar(),
}

# GUI Elements
row = 0
for feature in inputs:
    Label(window, text=f"Enter {feature.replace('_', ' ').capitalize()}:").grid(row=row, column=0, padx=10, pady=5,
                                                                                sticky='w')
    Entry(window, textvariable=inputs[feature]).grid(row=row, column=1, padx=10, pady=5)
    row += 1


# Function to preprocess inputs and make predictions
def predict():
    try:
        # Collect user inputs
        input_data = {key: val.get() for key, val in inputs.items()}

        # Validate inputs
        if not input_data['age'].isdigit():
            raise ValueError("Age must be a valid number.")

        # Convert inputs to a DataFrame
        df_input = pd.DataFrame([input_data])

        # Preprocess categorical features
        for column in ['sample_id', 'patient_cohort', 'sample_origin', 'sex']:
            if column in df_input:
                le = label_encoders[column]
                df_input[column] = le.transform(df_input[column])

        # Convert age to numeric and standardize
        df_input['age'] = pd.to_numeric(df_input['age'])
        df_input[['age']] = scaler.transform(df_input[['age']])

        # Make prediction
        prediction = model.predict(df_input)
        diagnosis = label_encoders['diagnosis'].inverse_transform(prediction)

        # Display the result
        messagebox.showinfo("Prediction Result", f"Diagnosis: {diagnosis[0]}")
    except KeyError as e:
        messagebox.showerror("Error", f"Invalid input for: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Predict Button
Button(window, text="Predict Diagnosis", command=predict).grid(row=row, column=0, columnspan=2, pady=20)

# Run the Tkinter event loop
window.mainloop()
