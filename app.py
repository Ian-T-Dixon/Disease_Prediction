from flask import Flask, request, render_template
import numpy as np
import json, pickle

import urllib.parse
from sqlalchemy import create_engine
import psycopg2

import sys, os
sys.path.append(os.path.abspath(os.path.join('../..')))
from config import db_password

app = Flask(__name__)

# Unpickle trained ML model
model = pickle.load(open('./static/data/svm_model.pkl', 'rb'))

# Store SQL connection string
db_string = f"postgresql://postgres:{urllib.parse.quote(db_password)}\
@127.0.0.1:5432/disease_prediction"

# Get column names from model training set and store as list
with create_engine(db_string).connect() as engine:
    result = engine.execute("SELECT * FROM dataset_bool WHERE False").keys()
    symptom_list = [x for x in result][1:]

# Save loaded symptoms from SQL query as json file
# Have Flask do this on startup to ensure compatibility
with open('./static/data/symptoms.json', 'w') as f:
    json.dump(symptom_list, f)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        # Receive dictionary of checked symptom names and Boolean values
        # Only True values are sent by form submission
        bool_dict = request.form.to_dict()

        # Fill in False values for the unchecked symptoms
        for symptom in symptom_list:
            if symptom not in bool_dict:
                bool_dict[symptom] = False

        # List of T/F for alphabetically sorted symptoms
        list_features = [True if bool(bool_dict[key]) else False
                         for key in sorted(bool_dict)]
        array_features = [np.array(list_features)]

        # Pass boolean array to model for prediction
        prediction = model.predict(array_features)[0]

        # Connect to SQL database to get more disease info
        with create_engine(db_string).connect() as engine:
            result = engine.execute(
                f"SELECT * FROM disease_info WHERE disease = '{prediction}'"
            )

            for row in result.mappings():
                lookup_desc = row["description"]
                lookup_care = [row[x] for x in
                ["precaution_1", "precaution_2",
                    "precaution_3", "precaution_4"]
                ]
                
        return render_template('predict.html',
			prediction_text=prediction,
			description_text=lookup_desc,
            precaution_1=lookup_care[0],
            precaution_2=lookup_care[1],
            precaution_3=lookup_care[2],
            external_link = f'https://www.webmd.com/search/search_results/default.aspx?query={prediction}'
            # placeholder_name = lookup_care[0]
		)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
