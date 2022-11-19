from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import json
from sklearn.metrics import (accuracy_score,
    confusion_matrix, ConfusionMatrixDisplay)
    
app = Flask(__name__)
model = pickle.load(open('./static/data/svm_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # requests data from POST and imports the symptom boolean dictionary produced from the form data.
    if request.method == "POST":
        bool_dict = request.get_json()
        
        list_features = [True if bool(bool_dict[key]) else False
        # Iterate through symptoms alphabetically
        for key in sorted(bool_dict)]
        array_features = [np.array(list_features)]

        # Pass boolean array to model for prediction
        prediction = model.predict(array_features)[0]
        print(prediction)
        return render_template('index.html', prediction_text="These symptoms appear to be caused by {}".format(prediction))
    
    
if __name__ == "__main__":
    app.run(debug=True)
