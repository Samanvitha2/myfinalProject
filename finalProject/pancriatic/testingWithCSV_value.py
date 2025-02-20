import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib  # Library to save and load the model

# Sample data
data = {
    'sample_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'patient_cohort': ['A', 'B', 'A', 'B', 'A'],
    'sample_origin': ['blood', 'tissue', 'blood', 'blood', 'tissue'],
    'age': [25, 40, 35, 50, 45],
    'sex': ['M', 'F', 'M', 'F', 'M'],
    'diagnosis': ['positive', 'negative', 'positive', 'negative', 'positive']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

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

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train[['age']] = scaler.fit_transform(X_train[['age']])
X_test[['age']] = scaler.transform(X_test[['age']])

# Test different SVM parameters
param_grid = {
    'kernel': ['linear', 'rbf', 'poly'],
    'C': [0.1, 1, 10],
    'gamma': ['scale', 'auto']
}

best_model = None
best_accuracy = 0
best_params = {}

for kernel in param_grid['kernel']:
    for C in param_grid['C']:
        for gamma in param_grid['gamma']:
            # Train the SVM classifier
            svm_model = SVC(kernel=kernel, C=C, gamma=gamma, random_state=42)
            svm_model.fit(X_train, y_train)

            # Evaluate the model
            y_pred = svm_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            print(f"Kernel: {kernel}, C: {C}, Gamma: {gamma}, Accuracy: {accuracy:.4f}")

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = svm_model
                best_params = {'kernel': kernel, 'C': C, 'gamma': gamma}

# Save the best model
joblib.dump(best_model, 'best_model.pkl')
print(f"Best model saved as 'best_model.pkl' with parameters: {best_params}")

# Save encoders and scaler for preprocessing during inference
joblib.dump(label_encoders, 'label_encoders.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Preprocessing components saved as 'label_encoders.pkl' and 'scaler.pkl'.")
