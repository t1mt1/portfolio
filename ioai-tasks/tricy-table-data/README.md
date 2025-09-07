# Time-Aware Imputation for Damaged Tabular Data

This project explores a regression task with heavily damaged and incomplete tabular data, tackled during my preparation for the International Olympiad in Artificial Intelligence (IOAI).

The dataset contains numeric features and timestamp-like fields (`day`, `hour`, `minute`). The evaluation metric is squared RMSE.

## Key Idea

Many features showed **time-dependent patterns**, with standard deviation varying across `(day, hour)` groups. I leveraged this structure to impute missing values **only in the test set**, using per-hour group means.

## Techniques Used

- Time-based feature imputation
- Gradient boosting with LightGBM
- Power transforms to align with evaluation metric (`target**0.25` for training, then inverted via `x**4`)
- Relative standard deviation analysis to identify temporal structure

## Files

- `imputation.ipynb`: Main notebook with full code, experiments, and comments

## Dataset

- `train_tables.csv`, `test_tables.csv`, `sample_submission.csv`
- From: (https://www.kaggle.com/competitions/neoai-2025-tricy-table-data/data)
