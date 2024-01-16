import pandas as pd

# อ่านข้อมูลจากไฟล์ Excel
file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(file_path)

# สร้าง Dummy Variables สำหรับคอลัมน์ 'province'
province_mapping = {
    1: 'Krabi', 2: 'Chumphon', 3: 'Trang', 4: 'Nakhon_Si_Thammarat', 5: 'Narathiwat',
    6: 'Pattani', 7: 'Phangnga', 8: 'Phatthalung', 9: 'Phuket', 10: 'Yala', 11: 'Ranong',
    12: 'Songkhla', 13: 'Satun', 14: 'Surat_Thani'
}

data['province'] = data['province'].map(province_mapping)
dummy_province = pd.get_dummies(data['province'])

# รวมข้อมูล Dummy Variables เข้ากับ DataFrame หลัก
data = pd.concat([data, dummy_province], axis=1)

# ลบคอลัมน์ 'province' เนื่องจากเราสร้างเป็น Dummy Variables แล้ว
data.drop('province', axis=1, inplace=True)

import statsmodels.api as sm

# กำหนดตัวแปรตามที่ต้องการใช้ในโมเดล
predictors = ['flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4',
              'house', 'habitable', 'evacuated', 'transportation', 'benefit',
              'area', 'fishing', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'latitude', 'longitude']
response = 'Risk'

# สร้างตัวแปรตามคอลัมน์ที่กำหนด
X = data[predictors]
y = data[response]

# เพิ่ม intercept ในตัวแปรต้น
X = sm.add_constant(X)

# สร้างแบบจำลอง Multinomial Logistic Regression
model = sm.MNLogit(y, X)
result = model.fit()

# ทำนายค่า Risk และหาค่าความน่าจะเป็นที่สูงที่สุด
predicted_probs = result.predict(X)
predicted_classes = predicted_probs.idxmax(axis=1)

# สร้าง Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score

conf_matrix = confusion_matrix(y, predicted_classes)
accuracy = accuracy_score(y, predicted_classes)
print("Confusion Matrix:\n", conf_matrix)
print("Accuracy:", accuracy)
