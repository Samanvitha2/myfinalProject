import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib  # Library to save and load the model

# Load dataset
file_path = "newdataset.csv"  # Update the path to your CSV file
df = pd.read_csv(file_path)

# Check if required columns exist
required_columns = ['sample_id', 'patient_cohort', 'sample_origin', 'age', 'sex', 'diagnosis']
if not all(column in df.columns for column in required_columns):
    raise ValueError(f"The dataset must contain the following columns: {required_columns}")

# Encode categorical features
label_encoders = {}
for column in ['sample_id', 'patient_cohort', 'sample_origin', 'sex']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Separate features and target
X = df[['sample_id', 'patient_cohort', 'sample_origin', 'age', 'sex']]
y = df['diagnosis']

# Encode the target variable
y_encoder = LabelEncoder()
y = y_encoder.fit_transform(y)
label_encoders['diagnosis'] = y_encoder

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train[['age']] = scaler.fit_transform(X_train[['age']])
X_test[['age']] = scaler.transform(X_test[['age']])

# Train the SVM classifier
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Save the model
joblib.dump(svm_model, 'model.pkl')
print("Model saved as 'model.pkl'.")

# Save encoders and scaler for preprocessing during inference
joblib.dump(label_encoders, 'label_encoders.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Preprocessing components saved as 'label_encoders.pkl' and 'scaler.pkl'.")

# Make predictions
y_pred = svm_model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
