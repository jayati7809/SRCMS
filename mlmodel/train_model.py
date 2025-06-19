# Fetches data, trains the model, and saves it.
import pickle
from sklearn.linear_model import LogisticRegression
from dbhelper import fetch_data
from processor import preprocess_data

def train_and_save_model():
    """ Fetch data, preprocess, train, and save the chatbot model. """
    df = fetch_data()
    if df.empty:
        print("No training data found in MongoDB!")
        return

    X, y, vectorizer, label_encoder = preprocess_data(df)
    model = LogisticRegression()
    model.fit(X, y)


    # Save the trained model and vectorizer
    with open("../models/chatbot_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("../models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("../models/label_encoder.pkl", "wb") as f:
        pickle.dump(label_encoder, f)

    print(" Model and vectorizer saved successfully!")

if __name__ == "__main__":
    train_and_save_model()









