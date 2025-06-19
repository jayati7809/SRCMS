from flask import Flask, request, jsonify
from utils.model_helper import load_model_and_vectorizer
from cleantext import clean
import pickle

app = Flask(__name__)

# Load model, vectorizer, and label encoder
with open("../models/chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("../models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("../models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.route("/chat", methods=["POST"])
def chatbot_response():
    """API endpoint for chatbot interactions."""
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No input provided!"}), 400

    # Preprocess the user input
    from processor import clean_text, analyze_sentiment
    cleaned_input = clean_text(user_input)
    sentiment = analyze_sentiment(cleaned_input)

    # Vectorize the input
    transformed_input = vectorizer.transform([cleaned_input])
    prediction = model.predict(transformed_input)[0]
    response = label_encoder.inverse_transform([prediction])[0]

    # Modify response based on sentiment
    if sentiment == 'positive':
        response = f"😊 I'm so glad to hear that! {response}"
    elif sentiment == 'negative':
        response = f"😟 I'm really sorry you feel that way. {response}. Let me help you better."
    else:
        response = f"🙂 Sure! {response}"

    # Return response with sentiment
    return jsonify({"response": response, "sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)



