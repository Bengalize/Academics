# Data Screening and Preparation

This repository contains an R script designed for data screening and preparation. The script performs various checks and preprocessing steps to ensure data quality before analysis. Below is a summary of the script’s functionality and usage.

## Script Overview

The R script performs the following tasks:

1. **Load Libraries and Import Data**:
   - Load necessary libraries.
   - Import the dataset from a CSV file.

2. **Data Screening**:
   - **Accuracy**: Clip the `Begin` and `After` variables to a range of 2 to 100.
   - **Missing Data**: Identify and handle missing data, including replacing missing values with imputed values and managing rows with excessive missingness.

3. **Outlier Detection**:
   - Calculate Mahalanobis distances to identify outliers.
   - Remove outliers based on a cutoff value.

4. **Additivity**:
   - Compute and visualize correlation matrices.
   - Assess the relationship between variables to ensure linearity and additivity.

5. **Linearity**:
   - Check for linearity by comparing residuals to fitted values and using Q-Q plots.

6. **Normality**:
   - Visualize the distribution of key variables using histograms.

7. **Homogeneity/Homoscedasticity**:
   - Plot standardized residuals against fitted values to check for homoscedasticity.

## Prerequisites

Ensure you have the following R packages installed:
- `rio`
- `VIM`
- `mice`
- `Hmisc`
- `corrplot`

You can install these packages using the following commands:
```r
install.packages(c("rio", "VIM", "mice", "Hmisc", "corrplot"))
