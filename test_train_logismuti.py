from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


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

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the MultiNomial Logistic Regression Classifier
model = LogisticRegression(random_state=42, max_iter=1000, multi_class='multinomial', solver='lbfgs')

# Train the MultiNomial Logistic Regression model
model.fit(X_train, y_train)

# Save the trained model to a file

# Make predictions using the trained MultiNomial Logistic Regression model on both train and test sets
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Evaluate the model on the train set
train_accuracy = accuracy_score(y_train, train_predictions)
train_classification_report = classification_report(y_train, train_predictions)

# Evaluate the model on the test set
test_accuracy = accuracy_score(y_test, test_predictions)
test_classification_report = classification_report(y_test, test_predictions)

# Display the results
print(f"Train Accuracy: {train_accuracy * 100: .2f} %")
print("Train Classification Report:")
print(train_classification_report)

print(f"\nTest Accuracy: {test_accuracy * 100:.2f} %")
print("Test Classification Report:")
print(test_classification_report)
