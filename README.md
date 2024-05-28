# Hate Speech Classification App

## Introduction

Welcome to the Hate Speech Classification App! This application allows users to input a comment and receive the corresponding hate speech category. The app leverages a deep learning model to classify comments into various categories of hate speech, namely reactionary,hate and violence, discrimination, self-harm, gambling, and prostitution, thus providing a valuable tool for content moderation and analysis.

## Technical Overview

This application is built using a combination of Python, Flask, Streamlit, and PostgreSQL. Below is an overview of the key components:

- **Flask**: Serves as the backend API for handling requests, processing classifications, and interacting with the database.
- **Streamlit**: Provides an intuitive and interactive web interface for users to input comments and view results.
- **PostgreSQL**: Manages the storage of user comments, classifications, and historical data.
- **Deep Learning Model**: Utilizes PHOBert, as at the time of conducting the research, it achieved SOTA results on tasks on Vietnamese. However, as time passes, there might be superior models. 

## How to Install

To get started, follow these steps: 

### Prerequisites

Ensure you have the following installed on your system(I use WSL):
- Python 3.7 or higher(For this application, I use python 3.10)
- Docker
- Docker Compose
- PostgreSQL

### Detailed how-to
First, clone the repository: 

```sh
git clone https://github.com/meredithoopis/ViHateCategorizer.git 
cd hate-speech-classification-app
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


