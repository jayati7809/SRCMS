from flask import Flask, render_template, request
import sqlite3  # Example database, change as needed

app = Flask(__name__)

# Connect to Database
def get_complaint_info(user_input):
    conn = sqlite3.connect("C:\Users\Jayati Basu\Documents\mydatabase.db")  # Change DB if needed
    cursor = conn.cursor() 
    
    # Query to fetch relevant complaint responses
    cursor.execute("SELECT response FROM complaints WHERE query LIKE ?", ('%' + user_input + '%',))
    result = cursor.fetchone()
    
    conn.close()
    
    return result[0] if result else "Sorry, I couldn't find an answer. Please contact support."

@app.route("/") 
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    return get_complaint_info(user_input)  # Only fetching from DB now

if __name__ == "__main__":
    app.run(debug=True) 


    

