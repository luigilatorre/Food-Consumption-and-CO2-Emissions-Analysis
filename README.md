# Food Consumption and CO2 Emissions Analysis

## Project Overview
This project analyzes the relationship between food consumption across various food categories and their associated CO2 emissions. The data used comes from the [`food_consumption.csv`](/data/food_consumption.csv) file located in the `/data` folder.

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
The calculations and data analysis are implemented in a Python script named [`food_consumption_analysis.py`](/data/food_consumption_analysis.py), which is located in the `/data` folder of this repository.
