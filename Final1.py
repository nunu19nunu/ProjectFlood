import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data from Excel file into a DataFrame
excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)

# Selecting relevant columns for analysis
selected_columns = ['Risk', 'province', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house', 'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]
data = data[selected_columns]

# Create dummy variables for 'province' column
dummy_provinces = pd.get_dummies(data['province'], prefix='province')
data = pd.concat([data, dummy_provinces], axis=1)
data.drop('province', axis=1, inplace=True)  # Drop the original 'province' column

# Define features (X) and target (y)
X = data.drop('Risk', axis=1)  # Features are all columns except 'Risk'
y = data['Risk']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# Create a new DataFrame with the desired features for prediction
new_data = pd.DataFrame({
    'province_1': [0],
    'province_2': [1],
    'province_3': [0],
    'province_4': [0],
    'province_5': [0],
    'province_6': [0],
    'province_7': [0],
    'province_8': [0],
    'province_9': [0],
    'province_10': [0],
    'province_11': [0],
    'province_12': [0],
    'province_13': [0],
    'province_14': [0],
    'flooding': [1],
    'overflow': [0],
    'flashflood': [1],
    'feq2': [1],
    'feq3': [0],
    'feq4': [0],
    'house': [0],
    'habitable': [1],
    'evacuated': [1],
    'transportation': [1],
    'benefit': [1],
    'area': [0],
    'fishing': [1],
    'Jan': [1],
    'Feb': [1],
    'Mar': [0],
    'Apr': [0],
    'May': [0],
    'Jun': [1],
    'Jul': [1],
    'Aug': [0],
    'Sep': [1],
    'Oct': [1],
    'Nov': [0],
    'Dec': [0],

})

# Get the names of features used in model training
features_used_in_training = X_train.columns.tolist()

# Create a new DataFrame with only the features used in model training
testdata_filtered = new_data[features_used_in_training]

# Make predictions for risk level
predicted_province = model.predict(testdata_filtered)

print("Risk Level:", predicted_province)

# Calculate accuracy on the test set
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)



# ทำการทำนายจังหวัด


