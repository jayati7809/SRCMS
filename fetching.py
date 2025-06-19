from pymongo import MongoClient
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

nltk.download("punkt")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update if needed
db = client["chatbot_db"]
collection = db["chat_data"]

# Load data from MongoDB
data = list(collection.find({}, {"_id": 0, "question": 1, "answer": 1}))

# Convert to DataFrame
df = pd.DataFrame(data)

# Text processing
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["question"])
y = df["answer"]

# Train ML model
model = LogisticRegression()
model.fit(X,y)

# Save the model and vectorizer
pickle.dump(model, open("chatbot_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model training complete!")nonlocal

 