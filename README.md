# Disease Prediction

There are many people around the world suffering from various diseases. These diseases, each requiring unique treatment, can be diagnosed by the symptoms that they cause. We have created a machine learning model that can make accurate disease predictions using symptoms experienced. This trained model can be deployed to a webpage to accept user inputs and make real-time predictions. A database is simultaneously queried to load stored information on the predicted illness, including treatment options. We showcase how ETL data analysis, full-stack development, and machine learning can be used to impact human well-being in the future of healthcare.

[Google Slides](https://docs.google.com/presentation/d/17sEjf6EPZSJ9EY5Vl9RA3tWl3OAGQc6XCYFe-FfR_w0/edit?usp=sharing) was used to present our development journey and findings to our mentors and peers.

## Installing and Running Locally

Run the following in the root folder to create the necessary virtual environment:
```
conda create -n disease-prediction --file spec-file.txt
```
<!--
This doesn't seem to work. It should be done in a new virtual environment.
```
pip install -r requirements.txt
```
 -->

Rename '[config_blank.py](config_blank.py)' to 'config.py' and move it to the folder grandparent to the local repo folder on your machine. Store credentials for your local Postgres database in this file.

Play through the [exploratory_analysis](exploratory.ipynb), [machine_learning](machine_learning.ipynb), and [csv_to_sql](csv_to_sql.ipynb) notebooks to upload the DataFrames to the local database.

We plan to use Heroku to publicly host the project webpage and database.

## Technologies Used

* Python, Pandas, Matplotlib, Pickle

* PostgreSQL, pgAdmin, SQLAlchemy

* scikit-learn, Decision Tree, Support Vector Machine

* HTML, CSS, JavaScript, Flask REST API

<!-- * Publicly hosted using Heroku Dynos and Heroku Postgres -->

## Data Pipeline

<!-- This section should stay written in the present tense. -->

1. Dataset is first cleaned of typographical errors and replacements are made to values for clarity.

2. Cleaned dataset is uploaded to SQL database using SQLAlchemy.

3. Cleaned dataset is loaded from database.

4. Cleaned dataset is tranformed to Boolean values for each symptom.

5. Machine learning model is trained on encoded data.

6. Trained machine learning model is saved as a pickle file.

7. Flask hosts website dashboard where user selects any experienced symptoms and submits a form.

8. POST request sent to Flask with Boolean for each symptom.

<!-- In this context, the absence of a parameter is equivalent to it being False -->

9. Flask uses unpickled model to make disease prediction from symptoms.

10. SQLAlchemy is used to lookup the disease from the database to retrieve description and precautions.

11. _To be implemented:_ Flask server may also use a stored version of model's confusion matrix to suggest possible differential diagnosis.

12. Information returned by POST request is used to update website dashboard with disease information.

## Dataset

The original dataset contains 4 tabular files:

* [Disease Dataset](./Data/Cleaned/dataset_clean.csv) consists of 41 diseases and 131 possible symptoms. Each disease has 120 cases or incidences.

* [Disease Description](./Data/Cleaned/disease_description_clean.csv) is a list of the diseases with a brief description of each illness.

* [Disease Precaution](./Data/Cleaned/disease_precaution_clean.csv) is a list of precautions to take for each disease.

* [Symptom Severity](./Data/Cleaned/symptom_severity_clean.csv) is a list of all symptoms with a weight to indicate severity.

Two more tables are created from the existing data:

* [Disease Info](./Data/Cleaned/disease_info.csv) is the result of joining Disease Description and Disease Precaution on name of Disease, and is used by Flask to give the end-user information on the predicted disease.

* [Boolean Dataset](./Data/Cleaned/dataset_bool.csv) is the encoded dataset (see After, below). To make predictions, the model expects symptoms passed in this format of Boolean per alphabetical symptom.

SQLAlchemy is used to update the database directly from Pandas DataFrames (rather than the exported .csv files).

## Data Cleaning & Processing

Using Python dictionaries and pandas.DataFrame.replace(), many replacements were made to the dataset for the sake of clarity and consistency. The main dataset of disease symptoms per case was then transformed to contain columns for every possible symptom, each containing Boolean values.

### **Before Encoding**
![data_df](./Images/data_df.png)

### **After Encoding**
![bool_df](./Images/bool_df.png)

Python readily interpets Boolean values as 1's and 0's. Consequently, this format is ready to be passed to the machine learning model, as it is already encoded and scaled.

## Machine Learning Model

Decision Tree Classifier was used as a benchmark classification model. Support Vector Classifier was investigated for superior performance. Support vector machines (SVM) work well on small datasets with clear separation between boundaries and don't perform as well on datasets with much noise.

The dataset was filled with many duplicates; removing these duplicates would drop the sample size for each disease from 120 to 5-10. Retaining these duplicates proved to make the models more robust against overfitting. The small effective size of the unduplicated dataset was mitigated by using a SVM classifier and using a 50/50 split between training and test data. sklearn's train_test_split() was used to create the training and testing datasets.

Decision Tree Classifier was trained with a max depth of 10 to prevent overfitting. Similarly, many values for the SVM 'gamma' and 'C' parameters were tried, until a model with a reasonable accuracy score and confusion matrix was returned. An [online introduction](https://vitalflux.com/svm-rbf-kernel-parameters-code-sample/) to these parameters was used to guide the selection of their values. The RBF kernel was used for the SVM due to its suitability for nonlinear data that is not well-known or characterized.

The decision tree benchmark performed decently at nearly 95% accuracy, yet the confusion matrix reveals a practical issue with the model: many illnesses are sometimes falsely predicted as heart attacks!

![clf_confusion_matrix](/Images/clf_confusion_matrix.png)

The support vector machine performs at a better 98% accuracy and has a less worrying confusion matrix. Variations of hepatitis are sometimes confused with each other or another liver illness, chronic cholestasis. Drug reaction is sometimes misdiagnosed as acne, which should be straightforward for the end user to distinguish. This model appears to perform well in the context of accurately and reasonably diagnosing illness based on reported symptoms.

![svm_confusion_matrix](/Images/svm_confusion_matrix.png)

Despite the above, the SVM model performed poorly when passed symptoms by the website end-user. One or two symptoms chosen at random usually resulted in a diagnosis of heart attack, producing a model prone to the same weaknesses as the Decision Tree Classifier. We postulate that the many varied symptoms demonstrated during heart attacks contribute to a large dimensional volume separating it from the symptom clusters more unique to other diseases.

RandomForestClassifier is currently used to supply predictions to the website dashboard, being the least worrisome upon passing more realistically random symptoms.

## Database

SQL was used to create a relational database with tables for the main dataset before and afer encoding, disease description and precautions, and symptom information.

The first step in loading the dataset into the SQL database is to create tables in a format comparable to the data that will populate those tables.

The four tables initially created are:
  - **"disease_cases"** (training dataset of symptoms per instance of disease) 
  - **"disease_descriptions"** (brief description of each disease in the dataset)
  - **"disease_precautions"** (list of precautions to take if facing threat of predicted disease)
  - **"symptom_severity"** (weights are ultimately disregarded. Categories are later assigned to each symptom for easier sorting on the website dashboard).

The following tables are created from this data:
* **"disease_info"** is created by joining the "disease_descriptions" and "disease_precautions" tables and gives the dashbend-user additional information on the predicted disease.
* **"dataset_bool"** is the encoded dataset used to train the machine learning model. The list of symptom checkboxes on the website dashboard is populated from its column names.

## Website Dashboard
The ML model, compiled and trained in Python, can deployed to a webpage using a Python server and Pickle, a module that faithfully loads saved ("pickled") Python objects. The webpage, hosted by Flask via Python, allows the user to input experienced symptoms and view the unpickled model's disease prediction. The Flask server also connects to the database using SQLAlchemy to lookup information about the disease, such as a description and suggested treatment options, pulled from the joined "**disease_info**" table. This information is then used to update the webpage and is displayed to the website end-user.

## Team Communication Protocol
The team met twice per week via Zoom during the main execution phase and uses Slack to communicate as needed. There is a Group Plan file to help document our goals and overall plan for the project.