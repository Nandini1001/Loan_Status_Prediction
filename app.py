from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET","POST"])
def home():

    prediction = None

    if request.method == "POST":

        gender = int(request.form["gender"])
        married = int(request.form["married"])
        dependents = int(request.form["dependents"])
        education = int(request.form["education"])
        self_emp = int(request.form["self_emp"])
        income = float(request.form["income"])
        co_income = float(request.form["co_income"])
        loan = float(request.form["loan"])
        term = float(request.form["term"])
        credit = int(request.form["credit"])
        property_area = int(request.form["property"])

        features = np.array([[gender, married, dependents, education,
                              self_emp, income, co_income, loan,
                              term, credit, property_area]])

        result = model.predict(features)

        if result[0] == 1:
            prediction = "Loan Approved ✅"
        else:
            prediction = "Loan Not Approved ❌"

    return render_template("index.html", prediction=prediction)


@app.route("/help")
def help():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(debug=True)