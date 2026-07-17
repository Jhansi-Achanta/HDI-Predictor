# 🌍 Human Development Index (HDI) Predictor

An AI & Machine Learning based web application that predicts the **Human Development Index (HDI)** of a country using **Linear Regression**. The application is built using **Python, Flask, Scikit-learn, Pandas, NumPy, Matplotlib, and Seaborn**.

---

## 📖 Project Overview

The Human Development Index (HDI) is a statistical measure used to evaluate a country's overall development based on three major dimensions:

- 🩺 Life Expectancy
- 🎓 Education
- 💰 Gross National Income (GNI) per Capita

This project predicts the HDI score using Machine Learning and displays the predicted development category.

---

## 🚀 Features

- Predicts HDI Score using Machine Learning
- Classifies countries into HDI categories:
  - 🌍 Very High Human Development
  - 🟢 High Human Development
  - 🟡 Medium Human Development
  - 🔴 Low Human Development
- Interactive Flask Web Application
- User-friendly Bootstrap Interface
- Data Visualization using Matplotlib and Seaborn
- Model saved using Pickle for fast predictions

---

## 🛠 Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- HTML
- CSS
- Bootstrap 5

---

## 📂 Project Structure

```
HDI-Predictor/
│
├── dataset/
│   └── HDI.csv
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── visualization.py
├── model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Machine Learning Workflow

1. Environment Setup
2. Dataset Collection
3. Data Understanding
4. Data Preprocessing
5. Exploratory Data Analysis (EDA)
6. Feature Selection
7. Train-Test Split
8. Linear Regression Model Training
9. Model Evaluation
10. Model Serialization using Pickle
11. Flask Web Application Development

---

## 📈 Input Features

- Life Expectancy at Birth
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) per Capita

---

## 📌 Output

The application predicts:

- HDI Score
- Human Development Category

Example:

```
HDI Score : 0.912

Category:
🌍 Very High Human Development
```

---

## 📊 Data Visualization

The project includes Exploratory Data Analysis (EDA) using:

- Heatmap
- Scatter Plot
- Distribution Plot
- Strip Plot
- Box Plot

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/HDI-Predictor.git
```

### Move into Project

```bash
cd HDI-Predictor
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python train_model.py
```

### Run Flask App

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🎯 Future Enhancements

- Add more Machine Learning algorithms
- Compare model performance
- Deploy the application online
- Add interactive dashboards
- Predict HDI for multiple countries simultaneously

---

## 👩‍💻 Developer

**Jhansi Naga Durga Achanta**

B.Tech – Computer Science & Engineering

Srinivasa Institute of Engineering and Technology

---

## 📜 License

This project is developed for educational and internship purposes.
