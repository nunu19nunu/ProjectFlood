import pandas as pd

excel_file_path = 'floodsouth.xlsx'
data = pd.read_excel(excel_file_path)

months = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน',
          'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']

for month in months:
    count_1 = data[month].sum()  # Count of occurrences of 1 in the current month
    count_0 = data[month].count() - count_1  # Count of occurrences of 0 in the current month
    total_count = data[month].count()  # Total number of values in the column (excluding NaN)

    percentage_1 = (count_1 / total_count) * 100
    percentage_0 = (count_0 / total_count) * 100

    print(f"Month: {month}")
    print(f"Percentage of flood occur: {percentage_1:.2f}%")
    print(f"Percentage of flood not occur: {percentage_0:.2f}%")
    print("--------------------------")

