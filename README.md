# Disease Prediction

The basis of this project is to use one or more machine learning models that can make accurate predictions of a disease by taking in arguments for symptoms (X) and predict the causative illness (y).

## Dataset

[Disease Prediction Dataset](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)

### Data Cleaning

* [symptom_Description.csv](./Data/symptom_Description.csv) and [symptom_precaution.csv](./Data/symptom_precaution.csv) can be merged to make them more useful for a user-application (see Dashboard section).

* Symptom descriptions will need to be cleaned to remove random spaces before and after each description and achieve uniformity.

## Machine Learning Model

Symptom severity should be included as feature in the ML model. [Symptom_Severity](/Data/Symptom-severity.csv) gives numerical weights to the severity of each symptom. 

Instead of the columns in the [dataset.csv](./Data/dataset.csv) being "symptom 1", "symptom 2", etc., they should be columns for every symptom, containing booleans (T/F).

For all .csv's: "Prognosis" should be removed as symptom (not a symptom, does not appear in dataset). "Scurring" should be replaced with "scarring". For clarity, "silver like dusting" should be replaced with "blue-gray complexion (argyria)".

## Dashboard
The trained ML model can be deployed to a webpage. Using Flask, we can build a simple webpage that will allow the user to input symptoms they are experiencing and view the model's prediction of their illness. Recommendations for treatment/precautions can be displayed, based on [symptom_precaution.csv](./Data/symptom_precaution.csv)
