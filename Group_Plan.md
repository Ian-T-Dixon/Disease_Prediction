# Group Plan

This is to journal our upcoming goals and overall plan for the project. Accomplishments will be reverted to past tense when complete instead of deleted. This documentation will help us present our process and challenges to our peers and potential clients.

## Data Pipeline

<!-- This section should stay written in the present tense. -->

1. Dataset is first cleaned of typographical errors and replacements are made to values for clarity.

2. Cleaned dataset is uploaded to SQL database.

3. ML model loads cleaned data from database using SQLAlchemy.

4. Cleaned dataset tranformed to boolean values for each symptom.

5. ML model is trained on encoded data.

6. ML model is saved as a pickle object.

7. Flask hosts webpage where user checks any experienced symptoms and submits.

8. REST API call sent to Flask with boolean for each symptom.

9. Flask uses unpickled model to make prediction.

10. SQLAlchemy is used to lookup the disease from the database to retrieve description and precautions.

11. API may also use a stored version of model's confusion matrix to suggest possible differential diagnosis.

12. JSON returned by API call used to update webpage with disease information.

## Data Cleaning

[disease_description.csv](./Data/disease_description.csv) and [disease_precaution.csv](./Data/disease_precaution.csv) can be merged. These would be useful for a user-application (see Dashboard, below). The DataFrames/tables should contain cleaned values before merging.

[symptom_severity.csv](/Data/symptom_severity.csv) gives numerical weights to the severity of each symptom. The severity could be included as feature in the ML model.

Instead of the columns in the [dataset.csv](./Data/dataset.csv) being "symptom 1", "symptom 2", etc., they should be loaded into the ML model as columns for every symptom (132), containing booleans (T/F).

The names of diseases and symptoms will be altered for clarity or typos in all four .csv files. Disease precautions will be similarly tidied. Those changes will be documented in the [data_changes](./Data/data_changes.md) file.

Give categories for each symptom in symptom_severity.csv
"Skin", "Mental", etc.

## Database

PostgreSQL, pgAdmin, SQLAlchemy

An SQL query was written to merge [disease_description.csv](./Data/disease_description.csv) and [disease_precaution.csv](./Data/disease_precaution.csv).

Optional: A table can be created with data from the ML model's confusion matrix.

## Machine Learning

Gaussian Radial Basis Function (RBF) is a kernel function that is highly preferred for non-linear data of unknown distribution.

## Dashboard

The trained ML model can be deployed to a webpage. Using Flask, we can build a simple webpage that will allow the user to input symptoms they are experiencing and view the model's prediction of their illness. Recommendations for treatment/precautions can be displayed, based on [disease_precaution.csv](./Data/disease_precaution.csv) and possibly the ML confusion matrix.