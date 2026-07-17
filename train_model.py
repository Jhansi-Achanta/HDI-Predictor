import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("dataset/HDI.csv")

# Select features
X = df[[
    "Life expectancy at birth - 2021",
    "Expected years of schooling - 2021",
    "Mean years of schooling - 2021",
    "Gross national income (GNI) per capita - 2021"
]]

# Target
y = df["Human Development Index (HDI) - 2021"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
from sklearn.metrics import r2_score

predictions = model.predict(X_test)

score = r2_score(y_test, predictions)

print("Accuracy :", round(score*100,2),"%")
print("Model Accuracy:", round(score * 100, 2), "%")

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")