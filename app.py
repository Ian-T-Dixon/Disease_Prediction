from flask import Flask, request, render_template
import numpy as np
import pickle
import csv

app = Flask(__name__)

# Unpickle trained ML model
# SWITCH back to svm_model after fixing 'acidity' symptom
model = pickle.load(open('./static/data/rfc_model.pkl', 'rb'))

# Read all possible symptoms into stored list
# TODO: Update this file with new symptom names
# May connect to SQL database instead for symptom names
with open('./static/data/symptoms_alpha.csv', newline='') as f:
    reader = csv.reader(f)
    symptom_list = sorted(
        [x[0] for x in reader][1:]      # [1:] ignores header
    )

# Save loaded symptoms from .csv or SQL query as json file
# Have Flask do this on startup to ensure compatability

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        # Receive dictionary of checked symptom names and Boolean values
        # Only True values are sent by form submission
        bool_dict = request.form.to_dict()

        # Fill in False values for the unchecked symptoms
        # symptoms.json should match the source of symptom_list
        for symptom in symptom_list:
            if symptom not in bool_dict:
                bool_dict[symptom] = False

        # List of T/F for alphabetically sorted symptoms
        list_features = [True if bool(bool_dict[key]) else False
                         for key in sorted(bool_dict)]
        array_features = [np.array(list_features)]

        # Pass boolean array to model for prediction
        prediction = model.predict(array_features)[0]

        return render_template('index.html',
			prediction_text='These symptoms appear to be caused by {}.'
				.format(prediction),
			# Any additional parameters to be updated on index.html
		)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
