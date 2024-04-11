import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load the dataset
file_path = '2023_Verified'  # Replace this with the path to your dataset
data = pd.read_csv(file_path+'.csv')

# Drop rows with missing values in the relevant columns
data = data.dropna(subset=['field_state', 'Commodity', 'soil_avg_soc'])

# Calculate the soil_soc_stock
data['soil_soc_stock'] = 10000 * 0.30 * data['soil_avg_bulkdensity'] * data['soil_avg_soc']

# Optionally, handle outliers in 'soil_avg_soc'
# This is just a placeholder for whatever outlier handling you choose to perform
# data = handle_outliers(data, 'soil_avg_soc')

# Filter the dataset for 'Soybeans' or 'Corn, Grain'
filtered_data = data[data['Commodity'].isin(['Soybeans', 'Corn, Grain'])]

# Ensure 'field_state' and 'Commodity' are categorical
filtered_data['field_state'] = filtered_data['field_state'].astype('category')
filtered_data['Commodity'] = filtered_data['Commodity'].astype('category')

# Add a new column for interaction groups
filtered_data['interaction_group'] = filtered_data['field_state'].astype(str) + "_" + filtered_data['Commodity'].astype(str)

# Tukey's HSD for Post Hoc analysis
tukey_results = pairwise_tukeyhsd(endog=filtered_data['soil_soc_stock'],
                                  groups=filtered_data['interaction_group'],
                                  alpha=0.05)

# Display the Tukey's HSD test results
print(tukey_results)

# Convert the Tukey's HSD results to a DataFrame
tukey_results_df = pd.DataFrame(data=tukey_results._results_table.data[1:], columns=tukey_results._results_table.data[0])

# Export the results to a CSV file
tukey_results_df.to_csv('results/'+file_path+'_tukey_hsd_results.csv', index=False)
