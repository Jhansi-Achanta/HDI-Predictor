import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder
os.makedirs("static/images", exist_ok=True)

# Load Dataset
df = pd.read_csv("dataset/HDI.csv")

# ----------------------------
# 1. Correlation Heatmap
# ----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include='number').corr(),
            annot=True,
            cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("static/images/heatmap.png")
plt.close()

# ----------------------------
# 2. Scatter Plot
# ----------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Life expectancy at birth - 2021",
    y="Human Development Index (HDI) - 2021",
    data=df
)
plt.title("Life Expectancy vs HDI")
plt.tight_layout()
plt.savefig("static/images/scatter.png")
plt.close()

# ----------------------------
# 3. Distribution Plot
# ----------------------------
plt.figure(figsize=(8,5))
sns.histplot(
    df["Human Development Index (HDI) - 2021"],
    kde=True
)
plt.title("HDI Distribution")
plt.tight_layout()
plt.savefig("static/images/distribution.png")
plt.close()

# ----------------------------
# 4. Strip Plot
# ----------------------------
plt.figure(figsize=(8,5))
sns.stripplot(
    y=df["Human Development Index (HDI) - 2021"]
)
plt.title("HDI Strip Plot")
plt.tight_layout()
plt.savefig("static/images/stripplot.png")
plt.close()

# ----------------------------
# 5. Box Plot
# ----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(
    y=df["Human Development Index (HDI) - 2021"]
)
plt.title("HDI Box Plot")
plt.tight_layout()
plt.savefig("static/images/boxplot.png")
plt.close()

print("All graphs generated successfully!")