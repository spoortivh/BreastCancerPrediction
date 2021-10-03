from flask import Flask,render_template,request,session
import pandas as pd

from sklearn.metrics import accuracy_score
import joblib

app = Flask(__name__)



@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def predict():
    return render_template('predict.html')

@app.route('/prediction1',methods =["POST","GET"])
def pred():
    s = []
    if request.method== "POST":
        radius = request.form['mr']
        textutre = request.form['mt']
        preimeter = request.form['mp']
        area = request.form['ma']
        smoothness = request.form['ms']
        compactness = request.form['mc']
        concavity = request.form['mcc']
        concave = request.form['mcp']
        symmetry = request.form['msy']
        fractal = request.form['mfd']
        s.extend([radius,textutre,preimeter,area, smoothness,compactness,concavity,concave,symmetry,fractal])
        model = joblib.load('scvmodeltraining.pkl')
        y_pred = model.predict([s])
        return render_template('predict.html',msg="success",op=y_pred)


if __name__ == '__main__':
    app.secret_key="hai"
    app.run(debug=True)
