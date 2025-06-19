import pickle

def load_model():
    """ Load the trained model and vectorizer from disk. """
    model = pickle.load(open("../models/chatbot_model.pkl", "rb"))
    vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))
    return model, vectorizer

#for using joblib library to import load model and vectorizer.
import joblib

def load_model_and_vectorizer():
    """Load the trained model and TF-IDF vectorizer using joblib."""
    model = joblib.load("../models/chatbot_model.pkl")
    vectorizer = joblib.load("../models/vectorizer.pkl")
    return model, vectorizer


## /preprocessing/preprocess.py
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_data(df):
    """ Clean and vectorize text data using TF-IDF. """
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["question"])  # Features
    y = df["answer"]  # Labels
    return X, y, vectorizer