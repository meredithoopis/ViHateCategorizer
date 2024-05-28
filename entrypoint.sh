#!/bin/sh
# Start the Flask API components and Streamlit app in the background

python app.py & 

streamlit run interface.py 


