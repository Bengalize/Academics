# Empirical Testing of Search Algorithms: Linear vs. Binary Search

## Overview
This project demonstrates the empirical testing of two fundamental search algorithms: **Linear Search** and **Binary Search**. The primary goal is to illustrate the Big-O efficiency of each algorithm by running a series of tests on arrays of varying sizes, measuring the time taken to find a specific element within these arrays.

## Why This Project is Useful
Understanding the efficiency of different search algorithms is crucial for optimizing performance in software development. This project provides a hands-on approach to comparing the time complexity of Linear Search (O(n)) and Binary Search (O(log n)) through practical implementation and data collection. By examining the results, developers can better understand when and why to use a particular search algorithm, especially when dealing with large data sets.

## What You Can Do with This Project
- **Learn about algorithm efficiency**: Gain practical insights into the time complexity of search algorithms.
- **Use the code as a benchmark**: Compare other search algorithms by adapting the provided framework.
- **Experiment with different data sizes**: Modify the array sizes, step sizes, and number of trials to see how the performance varies.
- **Generate CSV files**: Output the search times directly to a CSV file, which can be used for further analysis and graphing.

## How to Use This Project

### Prerequisites
- Python 3.x
- Basic understanding of Python programming
- Knowledge of algorithm time complexity (Big-O notation)

### Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/empirical-search-algorithms.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd empirical-search-algorithms
    ```

### Running the Program
1. **Run the Python script**:
    ```bash
    python empirical_testing.py
    ```
2. **Input the required parameters** when prompted:
    - `min_size`: The minimum size of the array to test.
    - `max_size`: The maximum size of the array to test.
    - `step_size`: The step size for increasing the array size.
    - `num_trial`: The number of trials to run for each array size.

3. **View the output**:
    - The program should generate a CSV file named `efficiency.csv` in the project directory, containing the results of the tests, including the array sizes and corresponding search times.

### Example CSV Output
The CSV file should have the following structure:
```csv
array_size, search_time
100, 1200
200, 2500
...
