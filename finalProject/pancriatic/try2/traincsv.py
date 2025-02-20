import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib  # Library to save and load the model

# Load dataset
file_path = "NewdatasetAfterStage.csv"  # Update the path to your CSV file
df = pd.read_csv(file_path)

# Check if required columns exist
required_columns = ['plasma_CA19_9', 'creatinine', 'LYVE1', 'REG1B', 'TFF1', 'REG1A', 'diagnosis']
if not all(column in df.columns for column in required_columns):
    raise ValueError(f"The dataset must contain the following columns: {required_columns}")

# Separate features and target
X = df[['plasma_CA19_9', 'creatinine', 'LYVE1', 'REG1B', 'TFF1', 'REG1A']]
y = df['diagnosis']

# Encode the target variable
y_encoder = LabelEncoder()
y = y_encoder.fit_transform(y)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the SVM classifier
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Save the model
joblib.dump(svm_model, 'model.pkl')
print("Model saved as 'model.pkl'.")

# Save the encoder and scaler for preprocessing during inference
joblib.dump(y_encoder, 'label_encoder.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Preprocessing components saved as 'label_encoder.pkl' and 'scaler.pkl'.")

# Make predictions
y_pred = svm_model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred ,zero_division=0))
