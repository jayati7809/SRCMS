import pymongo
import pandas as pd

def connect_mongo():
    """ Establish a connection to MongoDB. """
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client

def fetch_data():
    """ Retrieve chat data from MongoDB and return as a DataFrame. """
    client = connect_mongo()
    db = client["chatbot_db"]  # Database name
    collection = db["chat_data"]  # Collection name

    data = list(collection.find({}, {"_id": 0, "question": 1, "answer": 1}))
    df = pd.DataFrame(data)
    return df
