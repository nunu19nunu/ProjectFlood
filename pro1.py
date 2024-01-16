# Import Libraries
import pandas as pd
import numpy as np
# from patsy import dmatrices
# from statsmodels.discrete.discrete_model import MNLogit
# from sklearn.linear_model import LogisticRegression


# Load Data
# Please replace 'your_file_path.csv' with the actual file path of your dataset
excel_file_path = 'floodsouth v1.xlsx'
data = pd.read_excel(excel_file_path)
print(data.head())
# # Creating Dummy Variables
#
#
# # Assuming you have your data loaded into a DataFrame named 'floodsouth'
#
# # Create dummy variables in Python
# floodsouth['d1'] = np.where(floodsouth v1['province'] == 1, 1, 0)
# floodsouth['d2'] = np.where(floodsouth['province'] == 2, 1, 0)
# # Repeat this process for d3 to d13
#
# # Define independent and dependent variables
# y, X = dmatrices('Risk ~ d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + flooding + overflow + flashflood + feq2 + feq3 + feq4 + house + habitable + evacuated + transportation + benefit + area + fishing + Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec + latitude + longitude', data=floodsouth, return_type='dataframe')
#
# # Fit the multinomial logistic regression model
# model = MNLogit(y, X)
# result = model.fit()
#
# # Output Model Summary
# print(result.summary())
#
# # Prediction with new data
# test_data = pd.DataFrame({
#     'd1': [1],
#     'd2': [0],
#     'd3': [0],
#     # Continue adding values for d4 to d13 and other variables
#     'latitude': [8.17],
#     'longitude': [99.05]
#     # Add values for the remaining variables in your test data
# })
#
# # Make predictions
# predicted_probs = result.predict(test_data)
# print(predicted_probs)
#
#
# # Define Features and Target
# X = data[['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'flooding', 'overflow', 'flashflood', 'feq2', 'feq3', 'feq4', 'house', 'habitable', 'evacuated', 'transportation', 'benefit', 'area', 'fishing', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'latitude', 'longitude']]
# y = data['Risk']
#
# # Create and Train the Logistic Regression Model
# model = LogisticRegression(max_iter=1000)
# model.fit(X, y)
#
# # Calculate Accuracy
# accuracy = model.score(X, y)
# print("Accuracy:", accuracy)
#
# # Make Predictions
# # Replace the test data below with your actual test data for prediction
# test_data = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 8.17, 99.05]]
# predicted_probabilities = model.predict_proba(test_data)
# rounded_probabilities = [round(prob, 2) for prob in predicted_probabilities[0]]
# print("Predicted Probabilities:", rounded_probabilities)
