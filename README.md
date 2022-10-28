# Final_Project

A ML model can be trained to interpret a number of symptoms (X) and predict the causative illness (y). This trained model can then be deployed to a webpage to accept user inputs and make real-time predictions.

## Technologies Used

* Python (Pandas, Flask, SciKitLearn, Keras)
* SQL
* Flask
* D3.js (for dashboard, possibly)

## Data Cleaning and Analysis

Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

## Database Storage

SQL will be used as the database.

## Machine Learning

RandomForestClassifier will be used as a benchmark classification model. Support Vector Machines and Neural Networks will be investigated as viable multiclass classification models.

The model will use 132 boolean features as input and return one of 41 target diseases.

## Dashboard

The trained ML model can be deployed to a webpage. Using Flask, we can build a simple webpage that will allow the user to input symptoms they are experiencing and view the model's prediction of their illness. Recommendations for treatment/precautions can be displayed, based on [disease_precaution.csv](./Data/disease_precaution.csv). The illness most confused with the predicted illness can also be displayed, to assist with differential diagnosis.

## Teamwork

The team meets twice per week via Zoom and uses Slack to communicate as needed. There is a [Group Plan]() file to help document our upcoming goals and overall plan for the project.