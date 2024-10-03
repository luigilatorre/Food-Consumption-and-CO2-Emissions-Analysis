
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('data/food_consumption.csv')

# 1. Which food category has the highest median value of food consumption?
category_median = data.groupby('food_category')['consumption'].median().sort_values(ascending=False)
print('Food category with highest median consumption:')
print(category_median)

# 2. What is the interquartile range (IQR) for CO2 emissions by food category?
def calculate_iqr(group):
    return group.quantile(0.75) - group.quantile(0.25)

category_iqr = data.groupby('food_category')['co2_emission'].apply(calculate_iqr).sort_values(ascending=False)
print('\nInterquartile Range (IQR) for CO2 emissions by food category:')
print(category_iqr)

# 3. Which food category has the highest median CO2 emissions?
category_median_co2 = data.groupby('food_category')['co2_emission'].median().sort_values(ascending=False)
print('\nFood category with highest median CO2 emissions:')
print(category_median_co2)

# 4. Permutation test to compare poultry and fish consumption
poultry_consumption = data[data['food_category'] == 'poultry']['consumption']
fish_consumption = data[data['food_category'] == 'fish']['consumption']

# Observed difference in means
obs_diff_mean = poultry_consumption.mean() - fish_consumption.mean()

# Permutation test
diffs = []
combined = np.concatenate([poultry_consumption, fish_consumption])

for _ in range(1000):
    np.random.shuffle(combined)
    new_poultry = combined[:len(poultry_consumption)]
    new_fish = combined[len(poultry_consumption):]
    diffs.append(new_poultry.mean() - new_fish.mean())

diffs = np.array(diffs)
p_value = np.mean(diffs >= obs_diff_mean)

print(f'\nObserved difference in means: {obs_diff_mean}')
print(f'p-value: {p_value}')

# 5. Visualization - Boxplot of CO2 emissions by food category
plt.figure(figsize=(10, 6))
sns.boxplot(x='food_category', y='co2_emission', data=data)
plt.title('CO2 Emissions by Food Category')
plt.xticks(rotation=90)
plt.show()
