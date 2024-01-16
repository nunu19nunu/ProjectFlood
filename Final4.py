# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data from Excel file into a DataFrame
excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)

# Select relevant columns for analysis
selected_columns = ['Risk', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house', 'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'latitude', 'longitude']
data = data[selected_columns]

# Define features and target
X = data.drop('Risk', axis=1)  # Features are all columns except 'Risk'
y = data['Risk']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the new Logistic Regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# Train the new model
model.fit(X_train, y_train)

# Predict on the test set
logistic_predictions = model.predict(X_test)

# Calculate accuracy
accuracy_logistic = accuracy_score(y_test, logistic_predictions)
print(f"Accuracy Logistic: {accuracy_logistic * 100:.2f}%")
