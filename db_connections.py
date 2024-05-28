import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Establish connection to the PostgreSQL database using environment variables
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"), 
    user=os.getenv("USERNAME"), 
    password=os.getenv("PASSWORD"), 
    host=os.getenv("HOST"), 
    port=os.getenv("PORT")
)


def create_tables():
    """
    Create necessary tables if they do not exist.
    """
    with conn.cursor() as cur:
        # Create table for users
        cur.execute("""
        CREATE TABLE IF NOT EXISTS ngdung (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
        );
        """)
        print("Done")
        
        # Create table for communication records
        cur.execute("""
        CREATE TABLE IF NOT EXISTS giaotiep (
            id SERIAL PRIMARY KEY,
            text TEXT NOT NULL,
            label VARCHAR(50) NOT NULL,
            username VARCHAR(100) NOT NULL REFERENCES ngdung(username)
        );
        """)
        conn.commit()
        print("Done")

def get_user_by_username(username):
    """
    Retrieve a user by their username.
    
    Args:
        username (str): The username to search for.
    
    Returns:
        dict: The user data if found, None otherwise.
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM ngdung WHERE username = %s", (username,))
        user_data = cur.fetchone()
    return user_data

def create_user(username):
    """
    Create a new user with the given username.
    
    Args:
        username (str): The username for the new user.
    
    Returns:
        int: The ID of the newly created user.
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "INSERT INTO ngdung (username) VALUES (%s) RETURNING id",
            (username,)
        )
        user_id = cur.fetchone()['id']
        print(f"User created with ID: {user_id}")
        conn.commit()
    return user_id

def store_prediction(text, label, username):
    """
    Store a prediction result in the database.
    
    Args:
        text (str): The text that was classified.
        label (str): The classification label.
        username (str): The username of the user who submitted the text.
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "INSERT INTO giaotiep (text, label, username) VALUES (%s, %s, %s) RETURNING id",
            (text, label, username)
        )
        conn.commit()

def get_user_history(username):
    """
    Retrieve the classification history for a given user.
    
    Args:
        username (str): The username to retrieve history for.
    
    Returns:
        list: The classification history for the user.
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM giaotiep WHERE username = %s", (username,))
        history = cur.fetchall()
    return history

def get_stat_from_db():
    """
    Retrieve statistics about the classifications from the database.
    
    Returns:
        list: The statistics of classifications grouped by label.
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT label, COUNT(*) as count FROM giaotiep GROUP BY label")
        stats = cur.fetchall()
    return stats

# Create tables when the module is imported
create_tables()
