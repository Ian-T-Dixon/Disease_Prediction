# Group Plan

This is to journal our upcoming goals and overall plan for the project. Accomplishments will be reverted to past tense when complete instead of deleted. This documentation will help us present our process and challenges to our peers and potential clients.

## Data Cleaning

[disease_description.csv](./Data/disease_description.csv) and [disease_precaution.csv](./Data/disease_precaution.csv) can be merged. These would be useful for a user-application (see Dashboard, below). The DataFrames/tables should contain cleaned values before merging.

[symptom_severity.csv](/Data/symptom_severity.csv) gives numerical weights to the severity of each symptom. The severity could be included as feature in the ML model.

Instead of the columns in the [dataset.csv](./Data/dataset.csv) being "symptom 1", "symptom 2", etc., they should be loaded into the ML model as columns for every symptom (132), containing booleans (T/F).

The names of diseases and symptoms will be altered for clarity or typos in all four .csv files. Disease precautions will be similarly tidied. Those changes will be documented in the [data_changes](./Data/data_changes.md) file.

## Database

SQL

Week 2: An SQL query will need to be written to merge [disease_description.csv](./Data/disease_description.csv) and [disease_precaution.csv](./Data/disease_precaution.csv).

Week 3 or 4: A table can be created with data from the ML model's confusion matrix.

## Machine Learning

Week 1: Set up input/output skeleton of model.

Week 2: Data preprocessing, feature engineering, split train/test data, choose model.

## Dashboard

The trained ML model can be deployed to a webpage. Using Flask, we can build a simple webpage that will allow the user to input symptoms they are experiencing and view the model's prediction of their illness. Recommendations for treatment/precautions can be displayed, based on [disease_precaution.csv](./Data/disease_precaution.csv) and the ML confusion matrix.