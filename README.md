Vietnamese hatespeech classification 
===============================
A fine-tuned PhoBERT model on text classification with an accuracy score of 0.95

## HuggingFace model card
For simplicity, test the model by following this link: [lisa_model](https://huggingface.co/lisagrace/hate_speech_bert)

## Training the model
Navigate to the folder experimental_notebook, create a virtual environment( Python 3.9), and run the notebook. 

## Simple deployment
Clone this repository and create a virtual environment(Python 3.9) 
1. Install required packages: 
```bash
pip install -r requirement.txt
```
2. The trained model: Download the models from this Google Drive link and put them in the models directory: [Link](https://drive.google.com/drive/folders/15iEfry_iSTiZk6UpWiVwoyv7kjpEtb6w)

3. To start the elasticsearch service, change the directory to the main folder and run:
```bash
docker compose up -d
```
The service is available at "localhost:9200"

4. Open another terminal, to see the API run:
```bash
python main.py
```
If you want to see the UI through streamlit, open another terminal and run:  
```bash
python streamlit.py
```
Type a comment, or post a small paragraph to see whether the text is clean, or it is hatespeech in a particular category. 
