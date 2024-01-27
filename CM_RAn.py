from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


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

# Initialize the Gradient Boosting Classifier
model = RandomForestClassifier(random_state=42)

# Train the Gradient Boosting model
model.fit(X_train, y_train)

#Make predictions using the trained Gradient Boosting model on both train and test sets
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)


cm = confusion_matrix(y_test, test_predictions)

sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel('Predicted Class')
plt.ylabel('Actual Class')
plt.title('Confusion Matrix RandomForest')
plt.show()

cm = confusion_matrix(y_test, test_predictions)

# Display the confusion matrix
print("Confusion Matrix:")
print(cm)














