import streamlit as st
import requests
import pandas as pd

# Base URL for the API
BASE_URL = "http://localhost:5000"

# Function to classify text using the API
def classify_text(username, text):
    """
    Classifies the given text for a specified username.
    
    Args:
        username (str): The username of the user.
        text (str): The text to classify.
    
    Returns:
        str: The classification label of the text.
    """
    response = requests.post(f"{BASE_URL}/classify", json={"username": username, "text": text})
    if response.status_code == 200:
        try:
            response_json = response.json()
            label = response_json.get("label", "No label found")  # Extract the label
            return label
        except ValueError:  # Includes simplejson.decoder.JSONDecodeError
            st.error("Error: Response is not JSON")
            st.error(response.text)
            return None
    else:
        st.error(f"Error: {response.status_code}")
        st.error(response.text)
        return None

# Function to get user history from the API
def get_user_history(username):
    """
    Retrieves the classification history for a specified username.
    
    Args:
        username (str): The username of the user.
    
    Returns:
        list: The classification history of the user.
    """
    response = requests.get(f"{BASE_URL}/history", params={"username": username})
    try:
        return response.json()
    except ValueError:
        st.error("Error: Response is not JSON")
        st.error(response.text)
        return []

# Function to get statistics from the API
def get_statistics():
    """
    Retrieves the classification statistics from the API.
    
    Returns:
        list: The statistics of classifications.
    """
    response = requests.get(f"{BASE_URL}/statistics")
    try:
        return response.json()
    except ValueError:
        st.error("Error: Response is not JSON")
        st.error(response.text)
        return []

# Streamlit app title
st.title("Toxic Text Classification App")

# User input section in the sidebar
st.sidebar.title("User Information")
username = st.sidebar.text_input("Username")

# Ensure the username is provided
if username:
    # Text Classification Section
    st.subheader("Classify Text")
    text_input = st.text_area("Enter text to classify")
    if st.button("Classify"):
        classification_label = classify_text(username, text_input)
        if classification_label:
            st.write(f"Your toxic comment can be classified as {classification_label}")
        else:
            st.error("Failed to classify text")

    # User History Section
    st.subheader("User History")
    if st.button("Show History"):
        user_history = get_user_history(username)
        if user_history:
            history_df = pd.DataFrame(user_history)
            if not history_df.empty:
                st.dataframe(history_df)
            else:
                st.write("No history found for the user.")
        else:
            st.write("No history found for the user.")

    # Statistics Section
    st.subheader("Statistics")
    if st.button("Show Statistics"):
        statistics = get_statistics()
        if statistics:
            stats_df = pd.DataFrame(statistics)
            st.bar_chart(stats_df.set_index("label")["count"])
        else:
            st.write("No statistics available.")
else:
    # Warning if no username is provided
    st.sidebar.warning("Please enter a username to proceed.")
