# Food Consumption and CO2 Emissions Analysis

## Project Overview
This project analyzes the relationship between food consumption across various food categories and their associated CO2 emissions. The data used comes from the `food_consumption.csv` file located in the `/data` folder.

### Goals:
1. Identify which food category has the highest median value for consumption.
2. Visualize CO2 emissions by food category and find the one with the highest interquartile range (IQR).
3. Assess whether there is a statistically significant difference between poultry and fish consumption using a permutation test.

## Dataset:
- `food_consumption.csv`: Contains food consumption data by category for different countries, along with CO2 emissions data.

## Analysis Outline:

1. **Data Loading and Exploration**:
   - The dataset is loaded and basic exploration is performed to understand the structure and contents.

2. **Descriptive Statistics**:
   - Descriptive statistics for consumption metrics across food categories are generated.

3. **Boxplot Visualization**:
   - CO2 emissions for each food category are visualized using boxplots.

4. **Permutation Test**:
   - A permutation test is used to determine if the difference in consumption between poultry and fish is statistically significant.

## Key Findings:
- **Highest Consumption**: The food category with the highest median consumption is `dairy`.
- **CO2 Emissions**: The category with the highest IQR for CO2 emissions is `beef`.
- **Statistical Significance**: The permutation test shows that the difference in consumption between poultry and fish is statistically significant, and the null hypothesis is rejected.

## Python Code
The calculations and data analysis are implemented in a Python script named `food_consumption_analysis.py`, which is located in the `/data` folder of this repository.

You can import the functions defined in the `food_consumption_analysis.py` file into your Jupyter notebook or other Python scripts to reproduce the analysis.

### Example Usage:
Here is how you can use the code in the `food_consumption_analysis.py` file:

```python
# Importing the module
from data.food_consumption_analysis import (
    load_data, get_data_overview, get_unique_food_categories, get_country_count,
    get_consumption_statistics, plot_co2_boxplot, get_median_co2_for_beef,
    perform_permutation_test, plot_permutation_distribution
)

# Load the dataset
file_path = 'data/food_consumption.csv'
food_data = load_data(file_path)

# Overview of the data
get_data_overview(food_data)

# Unique food categories
print(get_unique_food_categories(food_data))

# Number of unique countries
print(get_country_count(food_data))

# Consumption statistics
consumption_stats = get_consumption_statistics(food_data)
print(consumption_stats)

# Boxplot of CO2 emissions
plot_co2_boxplot(food_data)

# Median CO2 emission for beef
print(get_median_co2_for_beef(food_data))

# Perform the permutation test between 'poultry' and 'fish'
mu_diff, p_value = perform_permutation_test(food_data, 'poultry', 'fish')
print(f"Difference in means: {mu_diff}")
print(f"P-value: {p_value}")
