from flask import Flask, request, jsonify
import os
import psycopg2
from psycopg2 import sql, DatabaseError
from classify import run_classification
from db_connections import store_prediction, get_user_history, get_stat_from_db, create_user, get_user_by_username

# Establish connection to the PostgreSQL database using environment variables
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"), 
    user=os.getenv("USERNAME"), 
    password=os.getenv("PASSWORD"), 
    host=os.getenv("HOST"), 
    port=os.getenv("PORT")
)

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def intro():
    """
    Introduction endpoint that provides information about the API.
    
    Returns:
        dict: A message describing the purpose of the API.
    """
    return {
        "message": "This simple API is designed for toxic speech classification. You can post a comment here and let the model decide which type of toxicity your comment belongs to."
    }

@app.route('/classify', methods=['POST'])
def classify_text():
    """
    Endpoint for classifying text as toxic or non-toxic.
    
    Expects JSON data with 'username' and 'text'. If the user does not exist, they are created.
    The text is classified, and the result is stored in the database.
    
    Returns:
        dict: The classified label for the provided text.
    """
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        username = data.get('username')
        text = data.get('text')
        if not username or not text:
            return jsonify({'error': 'Username and text are required'}), 400

        user = get_user_by_username(username)
        if not user:
            create_user(username)

        label = run_classification(text)
        store_prediction(text, label, username)
        return jsonify({'text': text, 'label': label})
    except (Exception, DatabaseError) as e:
        print(f"Error: {e}")
        conn.rollback()  # Rollback transaction if an error occurs
        return jsonify({'error': str(e)}), 500

@app.route('/history', methods=['GET'])
def user_history():
    """
    Endpoint for retrieving the classification history of a user.
    
    Expects a 'username' as a query parameter.
    
    Returns:
        list: The history of classifications for the specified user.
    """
    username = request.args.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    try:
        history = get_user_history(username)
        return jsonify(history)
    except (Exception, DatabaseError) as e:
        print(f"Error: {e}")
        conn.rollback()  # Rollback transaction if an error occurs
        return jsonify({'error': str(e)}), 500

@app.route('/statistics', methods=['GET'])
def get_statistics():
    """
    Endpoint for retrieving statistics about the classifications.
    
    Returns:
        dict: The statistics of classifications.
    """
    try:
        stats = get_stat_from_db()
        return jsonify(stats)
    except (Exception, DatabaseError) as e:
        print(f"Error: {e}")
        conn.rollback()  # Rollback transaction if an error occurs
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
