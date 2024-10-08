# CITS1401

## Data Processing and Analysis Scripts

This repository contains two Python scripts designed for comprehensive data cleaning and statistical analysis, with a focus on calculating averages, standard deviations, and correlations across monthly data. The scripts are particularly well-suited for datasets containing time-series data such as COVID-19 cases or similar epidemiological metrics.

### Project 1: Monthly Data Calculations

#### Description:
This script focuses on extracting meaningful insights from monthly time-series data. It is capable of calculating average values, standard deviations, and correlations across multiple variables in the dataset. 

- **Average Calculation**: The script computes the average for any specified month by iterating through the dataset and summing the values that match the month identifier. It is particularly useful for summarizing trends over time, such as the monthly average number of cases or deaths in epidemiological datasets. The function is robust and handles edge cases such as months with no data.
  
- **Standard Deviation**: This feature measures the variability of data for a given month. By applying the standard formula for standard deviation, the script calculates how much individual data points deviate from the computed monthly average. This is crucial for understanding the dispersion of data in a dataset where trends fluctuate significantly over time, allowing the user to gauge the consistency of recorded data.

- **Correlation**: The script includes a multi-step approach to calculate the correlation between two sets of data. This is helpful for comparing two variables over time to determine if there’s any relationship between them. For example, it could analyze the correlation between new cases and new deaths across different months. The correlation functions are split into smaller components that compute parts of the equation, improving code readability and modularity.

In summary, this script is built to process and analyze monthly data, allowing for detailed insight into patterns and variability, making it useful for epidemiologists, data scientists, or researchers looking to draw conclusions from large time-series datasets.

---

### Project 2: Data Cleaning Script

#### Description:
This script addresses common data quality issues in time-series datasets by ensuring that data is cleaned and formatted properly before analysis. Specifically, it focuses on:
  
- **Handling Missing or Incorrect Values**: Many datasets, particularly those related to real-world observations like COVID-19, may contain missing or incorrect values. For example, data points for new cases or deaths might be missing or recorded as non-numeric values. The script automatically detects and replaces these with default values (e.g., setting them to 0), ensuring that the dataset remains usable for analysis without requiring manual inspection.

- **Date Format Validation**: A common issue in time-series data is inconsistent or incorrect date formats. The script ensures that all date entries are in the proper `DD/MM/YYYY` format. It performs checks to identify and remove any entries with improper date formatting. This feature is particularly important for maintaining the integrity of time-series data, where out-of-order or malformed dates can lead to inaccurate analyses.

- **Cleaning Data for Specific Fields**: The script focuses on ensuring key fields (such as new cases and new deaths) are cleaned by converting non-numeric values to defaults and validating their presence across all entries. This ensures that the dataset is well-structured and ready for further analysis, reducing the likelihood of errors during statistical or trend analysis.

This data cleaning script is an essential tool for anyone working with real-world datasets that may suffer from inconsistencies, missing values, or formatting issues. By automating the cleaning process, it reduces the manual effort required to prepare the data for in-depth analysis or machine learning models.

---
