from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('heart_disease_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]
        prediction = model.predict([features])[0]
        result = '⚠️ Likely to have heart disease' if prediction == 1 else '✅ Unlikely to have heart disease'
    except Exception as e:
        result = f"Error: {str(e)}"
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
