import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model and feature names
model = joblib.load('randomForestModel.pkl')  # Load your model file

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
    1: "น้ำท่วม",
    0: "ไม่ท่วม"
}

features = ['ชื่อจังหวัด', 'ปีละครั้ง1มากกว่า', '2 ปีต่อครั้ง', '3 ปีต่อครั้ง', '4-9 ปีต่อครั้ง', '10 ปีต่อครั้ง1น้อยกว่า',
                'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม',
                'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']

district_names_to_keys = {v: k for k, v in district_labels.items()}

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
    col1, col2 = st.columns(2)
    for feature in features:
        if feature == 'ชื่อจังหวัด':
            district_select = st.selectbox('Select District', list(district_labels.values()))
            input_features[feature] = district_names_to_keys.get(district_select)
            st.write(f'Selected District: {district_select}')
            st.divider()
        else:
            user_input = st.radio(f'{feature}', list(binary_labels.values()), key=feature)
            input_features[feature] = next(key for key, value in binary_labels.items() if value == user_input)
            st.write(f'{feature}: {user_input}')
            st.divider()

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
