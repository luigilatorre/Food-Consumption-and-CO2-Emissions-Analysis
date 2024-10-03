# Food Consumption and CO2 Emissions Analysis

## Overview
This repository contains a data analysis project that examines food consumption and related CO2 emissions across various countries. The analysis is based on the **food_consumption.csv** dataset, and explores the relationships between different food categories and their environmental impact in terms of carbon dioxide emissions.

### Key Questions Addressed:
1. **Which food category has the highest median value of food consumption?**
2. **What is the interquartile range (IQR) for CO2 emissions by food category?**
3. **Which food category has the highest median CO2 emissions?**
4. **Is there a statistically significant difference between poultry and fish consumption?**

### Data and Code
The datasets used for this analysis are located in the `data/` folder:
- `distributions.csv`
- `food_consumption.csv`

The code to perform the analysis is provided in the [food_consumption_analysis.py](/data/food_consumption_analysis.py) file.

### Analysis Breakdown:
1. **Data Loading and Cleaning:**
   - The dataset is loaded and cleaned to prepare for analysis.
   - Basic descriptive statistics and initial visualizations are generated.

2. **Food Category Consumption:**
   - We analyze the food consumption per category, identifying the category with the highest median consumption.

3. **CO2 Emissions Analysis:**
   - Boxplots for each food category's CO2 emissions are generated, highlighting the highest IQR and median emissions.

4. **Statistical Testing:**
   - A permutation test is conducted to determine if the difference in consumption between poultry and fish is statistically significant.

### Instructions:
To run the analysis, you will need to:
1. Clone this repository.
2. Ensure you have the required Python libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`. 
