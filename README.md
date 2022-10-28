# Disease Prediction

The basis of this project is to use one or more machine learning models that can make accurate predictions of a disease by taking in arguments for symptoms (X) and predict the causative illness (y).

## Dataset

The dataset contains four CSV files.

* [Disease Dataset](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset) consists of 41 diseases and 132 possible symptoms. Each disease has 120 "cases"

* [Disease Description](./Data/symptom_Description.csv) is a list of the diseases with a brief description of each illness.

* [Symptom Severity](/Data/Symptom-severity.csv) is a list of all symptoms with a weight to indicate severity.

* [Symptom Precaution](./Data/symptom_precaution.csv) is a list of precautions to take for each disease.


### Data Cleaning

* Symptom description and Symptom precaution csv's can be merged to make them more useful for a user-application (see Dashboard section).

* Symptom descriptions will need to be cleaned to remove random spaces before and after each description and achieve uniformity. Can be achieve using the .strip() method.

* The Disease Dataset will need to have the columns changed from "Symptom 1", "Symptom 2" to instead have each column be a specific symptom with each row containing booleans (T/F).

* For all .csv's: "Prognosis" should be removed as symptom (not a symptom, does not appear in dataset). "Scurring" should be replaced with "scarring". For clarity, "silver like dusting" should be replaced with "blue-gray complexion (argyria)".

## Machine Learning Model

Random Forest Classifier will be used as a benchmark classification model. Support Vector Machines and Neural Networks will be investigated as viable multiclass classification models.

* Symptom severity gives numerical weights to the severity of each symptom, and should be used as a feature in our ML model.

## Database

SQL will be used to create a relational database with multiple tables for Disease Description, Disease Precautions, and the main dataset.

## Dashboard
The trained ML model can be deployed to a webpage. Using Flask/JavaScript, we can build a simple webpage that will allow the user to input symptoms they are experiencing and view the model's prediction of their illness. Recommendations for treatment/precautions can be displayed, based on [symptom_precaution.csv](./Data/symptom_precaution.csv) 

## Team Communication Protocol
The team meets twice per week via Zoom and uses Slack to communicate as needed. There is a Group Plan file to help document our upcoming goals and overall plan for the project.
