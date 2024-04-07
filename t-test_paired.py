#paired T-test

import pandas as pd
from scipy import stats

# Load the dataset
file_path = 'data/merged_dataset_2022.csv'  # Replace with your dataset's actual path
dataset = pd.read_csv(file_path)

# Paired T-Tests
# Ensure both columns exist in the dataset for the t-test
if 'delta_dSOC_ecosys' in dataset.columns:
    t_test_reduced = stats.ttest_rel(dataset['reduced_DNDC'], dataset['reduced_ecosys'])
    t_test_removed = stats.ttest_rel(dataset['removed_DNDC'], dataset['delta_dSOC_ecosys'])
else:
    t_test_reduced = None
    t_test_removed = None

# Statistical summary calculations
stats_summary = dataset[['reduced_DNDC', 'reduced_ecosys', 'removed_DNDC', 'delta_dSOC_ecosys']].agg(['max', 'min', 'mean', 'std']).transpose()

# Grouping by project, region, state, and county for summary information
project_summary = dataset.groupby(['Project', 'program_region', 'field_state', 'county_name']).agg(
    fields_count=('Field ID', 'nunique'),
    total_acres=('Acres', 'sum'),
    sum_reduced_DNDC=('reduced_DNDC', 'sum'),
    sum_reduced_ecosys=('reduced_ecosys', 'sum'),
    sum_removed_DNDC=('removed_DNDC', 'sum'),
    sum_delta_dSOC_ecosys=('delta_dSOC_ecosys', 'sum')
).reset_index()

# Exporting the project summary to a CSV file
output_file_path = 'data/summary.csv' 
project_summary.to_csv(output_file_path, index=False)

# Calculate and print the totals for each program region without truncating the columns
pd.set_option('display.max_columns', None)
region_totals = dataset.groupby('program_region').agg(
    total_reduced_DNDC=('reduced_DNDC', 'sum'),
    total_reduced_ecosys=('reduced_ecosys', 'sum'),
    total_removed_DNDC=('removed_DNDC', 'sum'),
    total_delta_dSOC_ecosys=('delta_dSOC_ecosys', 'sum')
).reset_index()

# Exporting the region totals to a CSV file
region_totals_output_path = 'data/region_totals.csv'  # Replace with your desired output path
region_totals.to_csv(region_totals_output_path, index=False)

# Output the results
print("Paired T-Test Results:")
print("Reduced DNDC vs. Reduced Ecosys:", t_test_reduced)
print("Removed DNDC vs. Delta dSOC Ecosys:", t_test_removed)

print("\nStatistical Summary:")
print(stats_summary)

print("\nProject Summary:")
print(project_summary)

print("\nTotals for Each Program Region:")
print(region_totals)
