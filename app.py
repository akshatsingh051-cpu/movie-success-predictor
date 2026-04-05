from flask import Flask, render_template, request
import pickle
import numpy as np
import matplotlib.pyplot as plt
from fetch_data import get_movie_data

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

# Feature importance graph
features = ['runtime','rating','votes','popularity','budget']
importances = model.feature_importances_

plt.figure()
plt.bar(features, importances)
plt.title("Feature Importance")
plt.savefig("static/importance.png")
plt.close()


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        movie_name = request.form["movie"]

        data = get_movie_data(movie_name)

        if data is None:
            return render_template("index.html", error="Movie not found")

        features_input = np.array([[
            data["runtime"],
            data["rating"],
            data["votes"],
            data["popularity"],
            data["budget"]
        ]])

        prob = model.predict_proba(features_input)[0][1] * 100

        if prob > 70:
            label = "🔥 Likely Hit"
        elif prob > 40:
            label = "⚖️ Average"
        else:
            label = "❌ Likely Flop"

        return render_template("index.html",
                               movie=data,
                               prediction=round(prob,2),
                               label=label)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)