import re
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from textblob import TextBlob

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
# Function to clean and preprocess text
def clean_text(text):
    # Lowercase text
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization (convert words to their root form)
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Return the cleaned text as a string
    return ' '.join(tokens)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Function to preprocess DataFrame
def preprocess_data(df):
    # Clean all questions in the DataFrame
    df['clean_text'] = df['question'].apply(clean_text)
    
    # Analyze sentiment of each question
    df['sentiment'] = df['clean_text'].apply(analyze_sentiment)
    
    # Vectorize the clean text
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['clean_text'])
    
    # Encode the labels (answers)
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(df['answer'])

    return X, y, vectorizer, label_encoder
