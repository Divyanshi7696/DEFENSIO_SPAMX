import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# If dataset has extra unnamed columns, clean it
df = df.iloc[:, :2]
df.columns = ["label", "message"]

# Convert labels if needed (optional safety)
df["label"] = df["label"].map({"spam": "spam", "ham": "ham"})

# Features and labels
X = df["message"]
y = df["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# SAVE MODEL + VECTORIZER
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model training complete and saved successfully!")