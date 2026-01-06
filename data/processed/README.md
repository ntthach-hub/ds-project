# Processed Data Directory

This directory contains cleaned and processed datasets ready for modeling.

## Guidelines

- Store preprocessed versions of raw data
- Include preprocessing scripts or notebooks that created these files
- Document any transformations applied

## Typical Preprocessing Steps

1. Handling missing values
2. Outlier treatment
3. Feature scaling/normalization
4. Encoding categorical variables
5. Feature engineering
6. Train-test split

## File Naming Convention

Use descriptive names that indicate the processing done:
- `dataset_name_cleaned.csv`
- `dataset_name_scaled.csv`
- `dataset_name_encoded.csv`
- `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`

## Note

Document the preprocessing steps in your notebooks or scripts for reproducibility.
