import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier


excel_file_path = 'floodsouth.xlsx'

data = pd.read_excel(excel_file_path)

# Mapping for 'ชื่อจังหวัด' column
district_labels = {
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
    # Add mappings for other districts...
}

print(list(district_labels.values()))
# Invert the district_labels dictionary to create a mapping from names to keys
district_names_to_keys = {v: k for k, v in district_labels.items()}

# Replace district names in the DataFrame column with their corresponding keys
data['ชื่อจังหวัด'] = data['ชื่อจังหวัด'].map(district_names_to_keys)
print(data['ชื่อจังหวัด'])

# Define features and target variable
features = ['ชื่อจังหวัด', 'ปีละครั้ง1มากกว่า', '2 ปีต่อครั้ง', '3 ปีต่อครั้ง', '4-9 ปีต่อครั้ง', '10 ปีต่อครั้ง1น้อยกว่า',
            'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม',
            'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
target = ['ระดับความเสี่ยง']

X = data[features]
y = data[target].values.ravel()

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the Random Forest model
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'randomForestModel.pkl')

# Make predictions using the trained Random Forest model
predictions = model.predict(X_test)

# Evaluate the Random Forest model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Get classification report for Random Forest
print(classification_report(y_test, predictions))

