import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load data from Excel file into a DataFrame
excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)

# Select relevant columns for analysis
selected_columns = ['Risk', 'province', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house',
                    'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar',
                    'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'latitude', 'longitude']
data = data[selected_columns]

# Define features and target
X = data.drop('Risk', axis=1)  # Features are all columns except 'Risk'
y = data['Risk']

# Initialize the RandomForestClassifier model
model = RandomForestClassifier()

# Fit the model with the entire dataset
model.fit(X, y)

# Input for prediction
province = input("กรุณาใส่ชื่อจังหวัด: ")
flooding = input("โรงพักอยู่ห่างจากแหล่งน้ำท่วม (ใส่ข้อความเช่น 'โรงพักอยู่ห่างจากแหล่งน้ำท่วม' หรือ 'ไม่มีน้ำท่วมไหลล้น'): ")
overflow = input("มีน้ำท่วมไหลล้น (ใส่ข้อความเช่น 'มีน้ำท่วมไหลล้น' หรือ 'ไม่มีน้ำท่วมไหลล้น'): ")
flashflood = input("มีน้ำท่วมไหลภายใน (ใส่ข้อความเช่น 'มีน้ำท่วมไหลภายใน' หรือ 'ไม่มีน้ำท่วมไหลภายใน'): ")
feq2 = input("เป็นเหตุการณ์ที่เกิดขึ้นครั้งที่ 2 (ใส่ข้อความเช่น 'เป็นเหตุการณ์ที่เกิดขึ้นครั้งที่ 2' หรือ 'ไม่เป็นเหตุการณ์ที่เกิดขึ้นครั้งที่ 2'): ")
# ... ตามลำดับคุณลักษณะอื่นๆ ...


# Make predictions
predicted_risk = model.predict(new_data)
predicted_province = new_data['province'].iloc[0]

# Display the prediction results
print(f"Predicted Province: {predicted_province}")
print(f"Predicted Risk: {predicted_risk}")
