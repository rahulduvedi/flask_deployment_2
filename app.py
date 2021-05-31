from flask import Flask,render_template,url_for,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",title = "home page" )

@app.route("/predict",methods = ["POST","GET"])
def predict():
    int_features =[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction = model.predict(final)
    output = prediction[0]
    if output == 1:
        return render_template('home.html',pred = "You have malignant cells")
    else:
        return render_template("home.html",pred = "you have benin cells")

if __name__ == "__main__":
       app.run(debug = True)
