import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the data
data = pd.read_csv("2022_TNCMN.csv")

# Checking for any inf or NaN values in the dataset and replacing them
data.replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace inf/-inf with NaN
data.dropna(inplace=True)  # Drop all rows with NaN values

# Selecting the independent and dependent variables
X = data[['baseline_residue', 'practice_residue', 'baseline_till_in', 'practice_till_in']]
y = data['removed']

# Adding a constant to the model (intercept)
X = sm.add_constant(X)

# Building the regression model
model = sm.OLS(y, X).fit()

# Print out the statistics
print(model.summary())
