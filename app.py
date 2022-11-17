from flask import Flask, request, render_template, jsonify
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('./static/data/svm_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output', methods=['POST'])

@app.route('/predict', methods=['POST'])
def predict():
    #reads checked box data from form and displays as JSON.
    symptoms = request.form.getlist("symptom")
    return jsonify(symptoms)
    

    
    
if __name__ == "__main__":
    app.run(debug=True)
