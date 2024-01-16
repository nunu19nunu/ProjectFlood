import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load data from Excel file into a DataFrame
excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)

# Selecting relevant columns for analysis
selected_columns = ['Risk', 'province', 'flooding', 'Water overflowing the banks', 'flash flood', '1year_more', '2year_more', '3year_more', '4-9 year_more', '10year_more', 'not flooding the house', 'buttheywerehabitable', 'had_to_be_evacuated', 'Transportation_routes', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data = data[selected_columns]

# Encoding the 'ชื่อจังหวัด' column

#
label_encoder = LabelEncoder()
data['province'] = label_encoder.fit_transform(data['province'])

# Define features and target

# data = pd.get_dummies(data, columns=['province'])  # Replace 'province' with your categorical column name

# Define features and target
# X = data.drop('Risk', axis=1)  # Features are all columns except 'Risk'
# y = data['Risk']
X = data[['province', 'flooding', 'Water overflowing the banks', 'flash flood', '1year_more', '2year_more', '3year_more', '4-9 year_more', '10year_more', 'not flooding the house', 'buttheywerehabitable', 'had_to_be_evacuated', 'Transportation_routes', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
y = data['Risk']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)

# Get classification report for evaluation
classification_rep = classification_report(y_test, predictions, output_dict=True)
class_labels = list(classification_rep.keys())[:-3]  # Extracting class labels

# Extract precision for each province class
precisions_by_province = {label: classification_rep[label]['precision'] for label in class_labels}

for province in range(1, 15):
    if str(province) not in precisions_by_province.keys():
        precisions_by_province[str(province)] = 0.0

sorted_precisions_by_province = {k: v for k, v in sorted(precisions_by_province.items(), key=lambda item: int(item[0]))}
# Plotting precision for each province
precision_table = pd.DataFrame(sorted_precisions_by_province.items(), columns=['Province', 'Precision'])
print(precision_table)
# Get classification report for evaluation
# print(classification_report(y_test, predictions))
# print(f"Accuracy: {accuracy}")

#
# # Example precision, recall, and f1-score for each class from your classification report
# precision = [1.00, 0.99, 0.96, 0.94, 0.99]
# recall = [1.00, 0.91, 0.94, 0.99, 0.99]
# f1_score = [1.00, 0.95, 0.95, 0.97, 0.99]
# Risk = ['1', '2', '3', '4', '5']
#
# # Plotting precision, recall, and f1-score for each class
# fig, ax = plt.subplots(figsize=(10, 6))
#
# bar_width = 0.2
# index = list(range(1, 6))
# opacity = 0.8
#
# rects1 = plt.bar(index, precision, bar_width, alpha=opacity, color='b', label='Precision')
# rects2 = plt.bar([i + bar_width for i in index], recall, bar_width, alpha=opacity, color='g', label='Recall')
# rects3 = plt.bar([i + 2 * bar_width for i in index], f1_score, bar_width, alpha=opacity, color='r', label='F1-score')
#
# plt.xlabel('Risk')
# plt.ylabel('Scores')
# plt.title('Metrics by Risk')
# plt.xticks([i + bar_width for i in index], Risk)
# plt.legend()
#
# plt.tight_layout()
#
#
#
#
# # Example class distribution (replace this with your actual class distribution)
# class_distribution = [330, 184, 538, 561, 345]
# Risk = ['1', '2', '3', '4', '5']
#
# plt.figure(figsize=(8, 8))
# plt.pie(class_distribution, labels=Risk, autopct='%1.1f%%', startangle=140)
# plt.title('Risk Class Distribution')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
#
#
# classification_rep = classification_report(y_test, predictions, output_dict=True)
# class_labels = list(classification_rep.keys())[:-3]  # Extracting class labels
#
# accuracies = [classification_rep[label]['precision'] for label in class_labels]
#
# # Plotting the line graph for accuracies
# plt.figure(figsize=(8, 6))
# plt.plot(class_labels, accuracies, marker='o', linestyle='-', color='blue')
# plt.title('Precision Across Classes')
# plt.xlabel('Classes')
# plt.ylabel('Precision')
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.tight_layout()
#
# # Show the line graph
# plt.show()
