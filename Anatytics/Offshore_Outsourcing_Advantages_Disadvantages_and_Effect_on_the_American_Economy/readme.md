# R Script for Analyzing Cost Savings Data

This repository contains an R script for analyzing cost savings data from a CSV file. The script performs various analyses, including generating frequency tables, histograms, z-scores, and identifying extreme values.

## Description

The R script performs the following tasks:
1. **Load Data**: Imports the dataset from a CSV file.
2. **Frequency Table**: Creates a frequency table for the percentage of outsourced jobs.
3. **Histograms**: Plots histograms for two cost savings methods.
4. **Z-Scores Calculation**: Computes z-scores for the cost savings methods.
5. **Extreme Z-Scores**: Identifies and counts the number of z-scores with a p-value < 0.05.
6. **Cost Savings Analysis**: Finds and prints the businesses with the highest and lowest cost savings and z-scores.

## Prerequisites

- R 
- `rio` package for data import

## Installation

1. Ensure you have R installed on your system.
2. Install the `rio` package if it's not already installed:

    ```r
    install.packages("rio")
    ```

