import pandas as pd

# Sample DataFrame
# data = {
#     'your_column': [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
# }
#
# df = pd.DataFrame(data)

excel_file_path = 'floodsouth.xlsx'
data = pd.read_excel(excel_file_path)


months = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน',
          'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']

# month = data.columns.tolist()

for month in months:
    count_1 = data[month].sum()  # Count of occurrences of 1 in the current month
    count_0 = data[month].count() - count_1  # Count of occurrences of 0 in the current month
    total_count = data[month].count()

# count_1 = data['มกราคม'].sum()  # Count of occurrences of 1
# count_0 = len(data) - count_1        # Count of occurrences of 0
#
# total_count = len(data)              # Total number of values in the column

percentage_1 = (count_1 / total_count) * 100
percentage_0 = (count_0 / total_count) * 100

print(f"Month: {month}")
print(f"Percentage of flood occur: {percentage_1:.2f}%")
print(f"Percentage of flood not occur: {percentage_0:.2f}%")
print("--------------------------")