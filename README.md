# 🎬 Movie Success Prediction Web App

A full-stack machine learning application that predicts whether a movie will be a **Hit or Flop** using real-time data.

---

## 🚀 Features
- 🔍 Search movie by name
- 🌐 Fetch real-time data using TMDb API
- 🤖 ML-based prediction (Hit / Flop)
- 📊 Probability score with confidence label
- 📈 Feature importance visualization
- 📉 Confusion matrix for evaluation

---

## 🧠 Tech Stack
- Python
- Flask
- Scikit-learn
- TMDb API
- HTML, CSS
- Matplotlib, Seaborn

---

## 📊 Model Details
- Algorithm: Random Forest Classifier
- Trained on real movie dataset
- Features used:
  - Runtime
  - Rating
  - Votes
  - Popularity
  - Budget

---

## 📁 Project Structure

```
movie-success-predictor/
│
├── app.py
├── train_model.py
├── fetch_data.py
├── model.pkl
├── movies_real.csv
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── importance.png
│   └── confusion.png
```


---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/movie-success-predictor.git
cd movie-success-predictor

pip install -r requirements.txt
python3 train_model.py
python3 app.py