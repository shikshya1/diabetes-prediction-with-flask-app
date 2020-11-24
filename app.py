import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('diabetic.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        pregnancy=int(request.form['pregnancy'])
        glucose=int(request.form['glucose'])
        skin=int(request.form['skin'])
        pressure=int(request.form['pressure'])
        insulin=int(request.form['insulin'])
        bmi=int(request.form['bmi'])
        dpf=int(request.form['dpf'])

        
        
        prediction=model.predict([[ age, pregnancy,glucose,skin,pressure,insulin,bmi,dpf]])
        
        if prediction>0:
            pred="You are at high risk of having diabetes"
        else:
            pred="You are at low risk of having diabetes"
            
        
        return render_template('index.html',prediction_text=pred)
    else:
        return render_template('index.html')

    
if __name__ == "__main__":
    app.run(debug=True)