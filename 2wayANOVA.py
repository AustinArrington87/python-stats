# 2 Way ANOVA

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the dataset
file_path = '2023_Verified'  # Replace this with the path to your dataset
data = pd.read_csv(file_path+'.csv')

# Filter the dataset for 'Soybeans' or 'Corn, Grain'
filtered_data = data[data['Commodity'].isin(['Soybeans', 'Corn, Grain'])]

# Perform two-way ANOVA
model = ols('soil_avg_ph ~ C(field_state) + C(Commodity) + C(field_state):C(Commodity)', data=filtered_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Display the ANOVA table
print(anova_table)

anova_table.to_csv('results/'+file_path+'ANOVA.csv', index=False)


# ALTERNATE Version without interaction terms 

# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.formula.api import ols

# # Load the 2022 dataset
# file_path = '2022_Verified'  # Replace this with the path to your dataset
# data = pd.read_csv(file_path+'.csv')

# # Filter the 2022 dataset for 'Soybeans' or 'Corn, Grain'
# filtered_data = data[data['Commodity'].isin(['Soybeans', 'Corn, Grain'])]

# # Perform two-way ANOVA without interaction terms
# model_no_interaction = ols('soil_avg_bulkdensity ~ C(field_state) + C(Commodity)', data=filtered_data).fit()
# anova_table_no_interaction = sm.stats.anova_lm(model_no_interaction, typ=2)

# # Display the ANOVA table
# print(anova_table_no_interaction)

# anova_table_no_interaction.to_csv('results/'+file_path+'ANOVA.csv', index=False)

