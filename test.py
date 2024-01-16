import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)

# change district to number===================================================>
unique_provinces = data['ชื่อจังหวัด'].unique()
province_to_number = {province: i + 1 for i, province in enumerate(unique_provinces)}
data['ชื่อจังหวัด'] = data['ชื่อจังหวัด'].map(province_to_number)
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

from sklearn.ensemble import RandomForestClassifier  # Import Random Forest Classifier

# ... (previous code remains the same)

# Initialize the Random Forest Classifier
model = LogisticRegression(multi_class='multinomial', max_iter=1000)

# Train the Random Forest model
model.fit(X_train, y_train)

# Make predictions using the trained Random Forest model
predictions = model.predict(X_test)

# Evaluate the Random Forest model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Get classification report for Random Forest
print(classification_report(y_test, predictions))


# Create custom data for prediction
custom_data = pd.DataFrame({
    'ชื่อจังหวัด': [3],
    'ปีละครั้ง1มากกว่า': [0],
    '2 ปีต่อครั้ง': [0],
    '3 ปีต่อครั้ง': [0],
    '4-9 ปีต่อครั้ง': [0],
    '10 ปีต่อครั้ง1น้อยกว่า': [0],
    'มกราคม': [0],
    'กุมภาพันธ์': [0],
    'มีนาคม': [0],
    'เมษายน': [0],
    'พฤษภาคม': [0],
    'มิถุนายน': [0],
    'กรกฎาคม': [0],
    'สิงหาคม': [0],
    'กันยายน': [0],
    'ตุลาคม': [0],
    'พฤศจิกายน': [0],
    'ธันวาคม': [0],

})

# Use the trained model to make predictions on the custom data
predictions_custom = model.predict(custom_data)

# Display predictions
print("Predictions for the custom data:")
print(predictions_custom)



