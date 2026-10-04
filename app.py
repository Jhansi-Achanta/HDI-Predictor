from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load ML model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    life = float(request.form["life"])
    expected = float(request.form["expected"])
    mean = float(request.form["mean"])
    gni = float(request.form["gni"])

    input_data = np.array([[life, expected, mean, gni]])

    prediction = model.predict(input_data)

    hdi_score = prediction[0]


    # HDI Classification

    if hdi_score >= 0.800:
        category = "🌍 Very High Human Development"

        message = (
            "This indicates excellent development with "
            "high life expectancy, education and income."
        )

    elif hdi_score >= 0.700:
        category = "🟢 High Human Development"

        message = (
            "This indicates good development with "
            "scope for further improvement."
        )

    elif hdi_score >= 0.550:
        category = "🟡 Medium Human Development"

        message = (
            "This indicates moderate development. "
            "Healthcare, education and income improvements are needed."
        )

    else:
        category = "🔴 Low Human Development"

        message = (
            "This indicates development challenges "
            "requiring major interventions."
        )


    return render_template(
        "index.html",
        prediction_text=f"HDI Score : {hdi_score:.3f}",
        category=category,
        message=message
    )


# Visualization Page

@app.route("/visualizations")
def visualizations():

    graphs = [
    "images/heatmap.png",
    "images/scatter.png",
    "images/distribution.png",
    "images/stripplot.png",
    "images/boxplot.png"
]

    return render_template(
        "visualizations.html",
        graphs=graphs
    )


if __name__ == "__main__":
    app.run(debug=True)