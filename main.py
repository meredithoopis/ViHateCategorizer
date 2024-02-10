from fastapi import FastAPI 
from pydantic import BaseModel 
import tasks 
from test_es import ES_DRIVER
import time 
import uvicorn

app = FastAPI()
            
@app.get('/') 
async def get_root(): 
    return {"message": "To run this text classification api, use the post method with the 'classify' route"}

@app.post("/classify") 
async def classify_text(text: str): 
    label = tasks.run_classification(text)
    tasks.store_prediction(text, label)
    return {"text": text, "prediction": label}

if __name__ == "__main__": 
    uvicorn.run("main:app", host = "0.0.0.0", port = 8000, reload=True)
