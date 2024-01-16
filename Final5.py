# import pandas as pd
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
#
# # Load data from Excel file into a DataFrame
# excel_file_path = 'floodsouth v1.xlsx'
# data = pd.read_excel(excel_file_path)
#
# # Select relevant columns for analysis
# selected_columns = ['Risk', 'province', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house',
#                     'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar',
#                     'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# data = data[selected_columns]
#
# # Define features and target
# X = data.drop('Risk', axis=1)  # Features are all columns except 'Risk'
# y = data['Risk']
#
# # Use pd.get_dummies() to convert 'province' column to dummy variables
#
# # Initialize an empty dictionary to store predictions and accuracy for each province
# # province_results = {}
# #
# # for province_name in data['province'].unique():
# #     # Filter data for the current province
# #     province_data = data[data['province'] == province_name]
# #
# #     # Define features and target for the current province
# #     X_province = province_data.drop('Risk', axis=1)
# #     y_province = province_data['Risk']
# #
# #     # Split data into train and test sets
# #     X_train, X_test, y_train, y_test = train_test_split(X_province, y_province, test_size=0.2, random_state=42)
# #
# #     # Initialize the RandomForestClassifier model
# #     model = RandomForestClassifier()
# #
# #     # Train the model
# #     model.fit(X_train, y_train)
# #
# #     # Predict on the test set
# #     predictions = model.predict(X_test)
# #
# #     # Calculate accuracy
# #     accuracy = model.score(X_test, y_test)
# #
# #     # Store predictions and accuracy for the current province in the dictionary
# #     province_results[province_name] = {
# #         'Predicted Risk': predictions.tolist(),
# #         'Accuracy': accuracy * 100
# #     }
#
# # # Display results for each province
# # for province, result in province_results.items():
# #     print(f"Province: {province}")
# #     print(f"Accuracy: {result['Accuracy']:.2f}%")
# #     print()
#
# def predict_province_result(province_input):
#     # Convert province name to province number
#     province_mapping = {
#         "กระบี่": 1,
#         "ชุมพร": 2,
#         "ตรัง": 3,
#         "นครศรีธรรมราช": 4,
#         "นราธิวาส": 5,
#         "ปัตตานี": 6,
#         "พังงา": 7,
#         "พัทลุง": 8,
#         "ภูเก็ต": 9,
#         "ยะลา": 10,
#         "ระนอง": 11,
#         "สงขลา": 12,
#         "สตูล": 13,
#         "สุราษฎร์ธานี": 14
#     }
#
#     # Check if the input is a number or province name
#     if isinstance(province_input, int):
#         selected_province = province_input
#     elif isinstance(province_input, str):
#         selected_province = province_mapping.get(province_input)
#
#     if selected_province is None:
#         print("Invalid province input. Please enter a valid province name or number.")
#         return
#
#     # Get the data for the selected province
#     province_data = data[data['province'] == selected_province]
#
#     X_province = province_data.drop('Risk', axis=1)
#     y_province = province_data['Risk']
#
#     X_train, X_test, y_train, y_test = train_test_split(X_province, y_province, test_size=0.2, random_state=42)
#
#     model = RandomForestClassifier()
#     model.fit(X_train, y_train)
#
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f"Province: {province_input}")
#     # print(f"Predicted Risk: {y_pred.tolist()}")
#     print(f"Accuracy: {accuracy * 100:.2f}%")
#
# # ให้ผู้ใช้ป้อน province ที่ต้องการ
# province_input = input("เลือกจังหวัดที่ต้องการ : ")
#
# # เรียกใช้ฟังก์ชันเพื่อแสดงผลลัพธ์สำหรับ province ที่ผู้ใช้เลือก
# predict_province_result(province_input)

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#โค้ดนี้ใช้สำหรับการนำเข้าไฟล์ข้อมูล Excel และเลือกเฉพาะคอลัมน์ที่เป็นประโยชน์
excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)

# Select relevant columns for analysis
selected_columns = ['Risk', 'province', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house',
                    'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar',
                    'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data = data[selected_columns]


#กำหนด features และ target variable ให้กับโมเดล
X = data.drop('Risk', axis=1)  # Features are all columns except 'Risk'
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
def predict_province_result():
    # Input values for prediction
    province_input = {
        'province': input("Enter province name: "),
        'flooding': int(input("Enter flooding value (0 or 1): ")),
        'overflow': int(input("Enter overflow value (0 or 1): ")),
        'flashflood': int(input("Enter flashflood value (0 or 1): ")),
        'feq2': int(input("Enter feq2 value (0 or 1): ")),
        'feq3': int(input("Enter feq3 value (0 or 1): ")),
        'feq4': int(input("Enter feq4 value (0 or 1): ")),
        'house': int(input("Enter house value (0 or 1): ")),
        'habitable': int(input("Enter habitable value (0 or 1): ")),
        'evacuated': int(input("Enter evacuated value (0 or 1): ")),
        'transportation': int(input("Enter transportation value (0 or 1): ")),
        'benefit': int(input("Enter benefit value (0 or 1): ")),
        'area': int(input("Enter area value (0 or 1): ")),
        'fishing': int(input("Enter fishing value (0 or 1): ")),
        'Jan': int(input("Enter Jan value (0 or 1): ")),
        'Feb': int(input("Enter Feb value (0 or 1): ")),
        'Mar': int(input("Enter Mar value (0 or 1): ")),
        'Apr': int(input("Enter Apr value (0 or 1): ")),
        'May': int(input("Enter May value (0 or 1): ")),
        'Jun': int(input("Enter Jun value (0 or 1): ")),
        'Jul': int(input("Enter Jul value (0 or 1): ")),
        'Aug': int(input("Enter Aug value (0 or 1): ")),
        'Sep': int(input("Enter Sep value (0 or 1): ")),
        'Oct': int(input("Enter Oct value (0 or 1): ")),
        'Nov': int(input("Enter Nov value (0 or 1): ")),
        'Dec': int(input("Enter Dec value (0 or 1): ")),
    }
    # Convert values to integers
    province_input = {key: int(value) for key, value in province_input.items()}

    # Get the data for the selected province
    province_data = data[data['province'] == province_input['province']]

    X_province = province_data.drop('Risk', axis=1)
    y_province = province_data['Risk']

    X_train, X_test, y_train, y_test = train_test_split(X_province, y_province, test_size=0.3, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    province_name = province_mapping[province_input['province']]
    print(f"Province: {province_name}")
    print(f"Accuracy: {accuracy * 100:.2f}%")

# Call the function to predict based on user input
predict_province_result()
