# Hate Speech Classification App

## Introduction

Welcome to the Hate Speech Classification App! This application allows users to input a comment and receive the corresponding hate speech category. The app leverages a deep learning model to classify comments into various categories of hate speech, namely reactionary,hate and violence, discrimination, self-harm, gambling, and prostitution, thus providing a valuable tool for content moderation and analysis.

## Technical Overview

This application is built using a combination of Python, Flask, Streamlit, and PostgreSQL. Below is an overview of the key components:

- **Flask**: Serves as the backend API for handling requests, processing classifications, and interacting with the database.
- **Streamlit**: Provides an intuitive and interactive web interface for users to input comments and view results.
- **PostgreSQL**: Manages the storage of user comments, classifications, and historical data.
- **Deep Learning Model**: Utilizes PHOBert, as at the time of conducting the research, it achieved SOTA results on tasks on Vietnamese. However, as time passes, there might be superior models. 

## Detailed how-to

To get started, follow these steps: 

### Prerequisites

Ensure you have the following installed on your system(I use WSL):
- Python 3.7 or higher(For this application, I use python 3.10)
- Docker
- Docker Compose
- PostgreSQL

### Setting up a PostgreSQL database for the app: 
In your terminal, do the following: 
Start the service: 
```sh
sudo service postgresql start
psql -U postgres
```

Create a new database and the new user as well as providing necessary privileges to put into the .env file below: 
```sh
CREATE USER new_user WITH PASSWORD 'password';
ALTER USER new_user WITH SUPERUSER;
CREATE DATABASE new_database;
GRANT ALL PRIVILEGES ON DATABASE new_database TO new_user;
```

### Running the application 
First, clone the repository: 

```sh
git clone https://github.com/meredithoopis/ViHateCategorizer.git 
cd ViHateCategorizer
```
Next, nagivate to the .env file to fill in necessary environment variables
```sh
SECRET_KEY="Create_your_own_secret_key"
DB_NAME="your_db_name"
USERNAME="your_username"
PASSWORD="your_username"
PORT="5432"
HOST="localhost"
```
Build and run with Docker Compose: 
```sh
docker compose up 
```

## Usage: 
Access the application for the interface: 
```sh
http://localhost:8501
```
### Classify a Comment
Enter your username in the sidebar.\
Type the comment you want to classify in the "Enter text to classify" text area.\
Click the "Classify" button to get the hate speech category for the comment.

### View User History
Enter your username in the sidebar.\
Click the "Show History" button under the "User History" section to view past classifications.

### View Statistics
Click the "Show Statistics" button under the "Statistics" section to view aggregated statistics of classifications.

### API Endpoints
The Flask API provides several endpoints for interacting with the application:
- **POST /classify**: Classify a given text comment.
- **GET /history**: Retrieve classification history for a specific user.
- **GET /statistics**: Get aggregated classification statistics.


