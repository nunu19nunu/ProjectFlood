import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

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

# Map for binary columns
binary_labels = {
    1: "Occur",
    0: "Not Occur"
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
model = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust the number of estimators (n_estimators) as needed

# Train the Random Forest model
model.fit(X_train, y_train)

# # Make predictions using the trained Random Forest model
# predictions = model.predict(X_test)
#
# # Evaluate the Random Forest model
# accuracy = accuracy_score(y_test, predictions)
# print(f"Accuracy: {accuracy}")
#
# # Get classification report for Random Forest
# print(classification_report(y_test, predictions))

# Create Streamlit app=================================================================>
st.title('Flood Risk Prediction')

expander = st.expander("About")
expander.write(
    "This app predicts the risk level of floods based on various parameters using a Random Forest Classifier."
)

with st.container():
    st.header('Random Forest Classifier')
    st.write('The model has been trained and is ready for predictions.')

    input_features = {}
    for feature in features:
        if feature == 'ชื่อจังหวัด':
            district_select = st.selectbox('Select District', list(district_labels.values()))
            input_features[feature] = district_names_to_keys.get(district_select)
            # st.write(f'Selected District: {district_select}')
        else:
            user_input = st.radio(f'{feature}', list(binary_labels.values()), key=feature)
            input_features[feature] = next(key for key, value in binary_labels.items() if value == user_input)
            # st.write(f'{feature}: {user_input}')

    # Add a button for prediction
    if st.button('Predict'):
        # Make a prediction based on user inputs
        input_data = pd.DataFrame([input_features])

        # Make prediction using the trained model
        prediction = model.predict(input_data)
        predicted_class = prediction[0]

        risk_level_labels = {
            1: 'Low',
            2: 'Moderate',
            3: 'Medium',
            4: 'High',
            5: 'Very High'
        }
        # Predict the risk level based on the predicted class
        predicted_risk_level = risk_level_labels[predicted_class]
        st.write('Predicted Risk Level:', predicted_risk_level)

        # Evaluate the Random Forest model
        accuracy = accuracy_score(y_test, prediction)
        st.write('Accuracy:', accuracy)

        # Get classification report for Random Forest
        st.write('Classification report:', classification_report(y_test, prediction))