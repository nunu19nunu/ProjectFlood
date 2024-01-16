# import streamlit as st
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# # Load data
# excel_file_path = 'floodsouth v1.xlsx'
# data = pd.read_excel(excel_file_path)
#
# # Select relevant columns
# selected_columns = ['Risk', 'province', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house',
#                     'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar',
#                     'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# data = data[selected_columns]
#
# # Define features and target
# X = data.drop('Risk', axis=1)
# y = data['Risk']
#
# province_mapping = {
#     1: "กระบี่",
#     2: "ชุมพร",
#     3: "ตรัง",
#     4: "นครศรีธรรมราช",
#     5: "นราธิวาส",
#     6: "ปัตตานี",
#     7: "พังงา",
#     8: "พัทลุง",
#     9: "ภูเก็ต",
#     10: "ยะลา",
#     11: "ระนอง",
#     12: "สงขลา",
#     13: "สตูล",
#     14: "สุราษฎร์ธานี"
# }
#
# # Function to predict province result
# def predict_province_result(province_input, other_inputs):
#     # Convert selected province back to code
#     province_code = {v: k for k, v in province_mapping.items()}[province_input]
#
#     # Get the data for the selected province
#     province_data = data[data['province'] == province_code]
#
#     X_province = province_data.drop('Risk', axis=1)
#     y_province = province_data['Risk']
#
#     # Convert other inputs to numerical values
#     for key, value in other_inputs.items():
#         if value == 'เสี่ยง':
#             other_inputs[key] = 1
#         else:
#             other_inputs[key] = 0
#
#     # Add your other input fields here
#     # ...
#
#     # Train the model
#     X_train, X_test, y_train, y_test = train_test_split(X_province, y_province, test_size=0.3, random_state=42)
#     model = RandomForestClassifier()
#     model.fit(X_train, y_train)
#
#     # Make predictions
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#
#     return accuracy
#
# # Streamlit app
# def main():
#     st.title("Flood Risk Prediction App")
#
#     # User input
#     province_input = st.selectbox("Select province:", [None] + list(province_mapping.values()))
#     other_inputs = {
#         'flooding': st.radio("Flooding:", options=['เสี่ยง', 'ไม่เสี่ยง']),
#         'overflow': st.radio("Overflow:", options=['เสี่ยง', 'ไม่เสี่ยง']),
#         'flashflood': st.radio("Flashflood:", options=['เสี่ยง', 'ไม่เสี่ยง']),
#         'feq2': st.radio()("Feq2:", options=['เสี่ยง', 'ไม่เสี่ยง']),
#         'feq3': st.radio()("Feq2:", options=['เสี่ยง', 'ไม่เสี่ยง']),
#     }
#
#     if st.button("Predict"):
#         # Display result
#         if province_input is None:
#             st.warning("Please select a province.")
#         else:
#             result_accuracy = predict_province_result(province_input, other_inputs)
#             st.text(f"{province_input}: {result_accuracy * 100:.2f}%")
#
# if __name__ == '__main__':
#     main()


import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

# Function to predict province result
def predict_province_result(province_input, other_inputs):
    # Convert selected province back to code
    province_code = {v: k for k, v in province_mapping.items()}[province_input]

    # Get the data for the selected province
    province_data = data[data['province'] == province_code]

    X_province = province_data.drop('Risk', axis=1)
    y_province = province_data['Risk']

    # Convert other inputs to numerical values
    for key, value in other_inputs.items():
        if value == 'เสี่ยง':
            other_inputs[key] = 1
        else:
            other_inputs[key] = 0

    # Train the model
    X_train, X_test, y_train, y_test = train_test_split(X_province, y_province, test_size=0.3, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

# Streamlit app
def main():
    st.title("Flood Risk Prediction App")

    # User input
    province_input = st.selectbox("Select province:", [None] + list(province_mapping.values()))
    other_inputs = {}

    # Create radio buttons for each variable
    for column in selected_columns[2:]:
        options = ['เสี่ยง', 'ไม่เสี่ยง']
        other_inputs[column] = st.radio(f"{column}:", options=options)

    if st.button("Predict"):
        # Display result
        if province_input is None:
            st.warning("Please select a province.")
        else:
            result_accuracy = predict_province_result(province_input, other_inputs)
            st.text(f"{province_input}: {result_accuracy * 100:.2f}%")

if __name__ == '__main__':
    main()
