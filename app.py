from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl",'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final = [np.array(features)]
    pred = model.predict(final)

    output = round(pred[0],2)

    return render_template("index.html",prediction_text=f"Employee salary should be ${output}")

if __name__ == "__main__":
    app.run(debug=True)