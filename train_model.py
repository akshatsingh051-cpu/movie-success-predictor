import os
import requests
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

API_KEY = "e13a7a6838106ae03166e838a801ef6e"

# 🔥 If dataset already exists → skip API
if os.path.exists("movies_real.csv"):
    print("Loading existing dataset...")
    df = pd.read_csv("movies_real.csv")

else:
    print("Fetching data from TMDb...")
    movies = []

    for page in range(1, 3):   # 🔥 reduced pages (more stable)
        try:
            url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={page}"
            response = requests.get(url, timeout=10).json()

            for m in response['results']:
                try:
                    movie_id = m['id']
                    details = requests.get(
                        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}",
                        timeout=10
                    ).json()

                    movies.append({
                        'runtime': details.get('runtime', 0),
                        'rating': details.get('vote_average', 0),
                        'votes': details.get('vote_count', 0),
                        'popularity': details.get('popularity', 0),
                        'budget': details.get('budget', 0),
                        'revenue': details.get('revenue', 0)
                    })

                    time.sleep(0.5)  # 🔥 VERY IMPORTANT

                except:
                    continue

        except:
            continue

    df = pd.DataFrame(movies)

    df = df[(df['runtime'] > 0) & (df['budget'] > 0)]
    df['hit'] = (df['revenue'] > df['budget']).astype(int)

    df.to_csv("movies_real.csv", index=False)
    print("Dataset saved!")

# ------------------ MODEL ------------------

X = df[['runtime','rating','votes','popularity','budget']]
y = df['hit']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.savefig("static/confusion.png")

pickle.dump(model, open("model.pkl", "wb"))

print("Model ready!")