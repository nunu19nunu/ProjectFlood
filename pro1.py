import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

# อ่านข้อมูลจากไฟล์ Excel
excel_file_path = 'floodsouth.xlsx'
data = pd.read_excel(excel_file_path)

# สร้างคอลัมน์ 'ds' จากวันที่เฉพาะวันแรกของแต่ละเดือน
data['ds'] = data['Month'].apply(lambda x: pd.to_datetime(f"{x}-01"))

# เลือกเฉพาะคอลัมน์ที่ต้องการ
data = data[['ds', 'y']]

# สร้างโมเดล Prophet
model = Prophet()

# ฝึกโมเดลด้วยข้อมูล
model.fit(data)

# สร้าง DataFrame สำหรับการทำนายล่วงหน้า
future = model.make_future_dataframe(periods=365)  # ทำนายล่วงหน้า 365 วัน

# ทำการทำนายล่วงหน้า
forecast = model.predict(future)

# แสดงผลลัพธ์
fig = model.plot(forecast)
plt.show()
