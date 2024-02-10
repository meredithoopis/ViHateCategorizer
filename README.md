# Vietnamese hatespeech classification 
A fine-tuned PhoBERT model on text classification with an accuracy score of 0.95

# HuggingFace model card
For simplicity, test the model by following this link: [Lisa_Hatespeech](https://huggingface.co/lisagrace/hate_speech_bert)

# Training the model
Navigate to the folder experimental_notebook and run the notebook. Create a virtual environment(Use python>==3.9)
# Simple deployment
Create a virtual environment(python==3.9)
To start the elasticsearch service, change the directory to the main folder and run "docker compose up": To check the elasticsearch cluster, run "curl localhost:9200" 
Open another terminal, run the file main.py to use the API service. Go to "localhost:8000" to see the API 
If you want to see the UI through streamlit, open another terminal and run the streamlit.py file. (Available through "localhost:8501"
Type a comment, or post a small paragraph to see whether the text is clean, or it is hatespeech in a particular category 
