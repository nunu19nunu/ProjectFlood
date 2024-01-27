import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

# Load data
excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)

# Select relevant columns
selected_columns = ['Risk', 'province', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house',
                    'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar',
                    'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data = data[selected_columns]

# Define features and target
X = data.drop('Risk', axis=1)

y = data['Risk']

province_mapping = {
    1: "กระบี่",
    2: "ชุมพร",
    3: "ตรัง",
    4: "นครศรีธรรมราช",
    5: "นราธิวาส",
    6: "ปัตตานี",
    7: "พังงา",
    8: "พัทลุง",
    9: "ภูเก็ต",
    10: "ยะลา",
    11: "ระนอง",
    12: "สงขลา",
    13: "สตูล",
    14: "สุราษฎร์ธานี"
}


# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the Random Forest model
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'randomforestv2.pkl')

# Make predictions using the trained Random Forest model
predictions = model.predict(X_test)
print(predictions)
# Evaluate the Random Forest model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Get classification report for Random Forest
print(classification_report(y_test, predictions))
