import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

excel_file_path = 'floodsouth.xlsx'

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



# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust the number of estimators (n_estimators) as needed

# Train the Random Forest model
model.fit(X_train, y_train)

# Make predictions using the trained Random Forest model
predictions = model.predict(X_test)

# Evaluate the Random Forest model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Get classification report for Random Forest
print(classification_report(y_test, predictions))

# Create Streamlit app=================================================================>
st.title('Flood Risk Prediction')

st.write('Random Forest Classifier is trained and ready for predictions.')

# Add inputs for features (you can customize this)
feature_inputs = {}
for feature in features:
    feature_inputs[feature] = st.number_input(f'Enter value for {feature}', value=0)

# Make a prediction based on user inputs
input_data = pd.DataFrame([feature_inputs])
prediction = model.predict(input_data)

st.write('Prediction:')
st.write(prediction)









