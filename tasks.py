from transformers import AutoTokenizer 
import torch 
from test_es import ES_DRIVER 
import os 


current_dir = os.getcwd()

#Model 1: Negative/clean 
torch_script_model_1 = torch.jit.load(os.path.join(current_dir, "models/Binary/Binary_model.pt"))
torch_script_model_1.eval()
tokenizer_1 = AutoTokenizer.from_pretrained(os.path.join(current_dir, "models/Binary/tokenizer/tokenizer_binary"))

#Model 2: 6 classes 
torch_script_model_2 = torch.jit.load(os.path.join(current_dir, "models/6_classes/tokenizer/Model_6.pt"))
torch_script_model_2.eval()
tokenizer_2 = AutoTokenizer.from_pretrained(os.path.join(current_dir, "models/6_classes/tokenizer/torchscript_model")) 

id2label = {0: "Reactionary", 1:"Hate and violence", 2: "Discrimination", 3: "Self-harm", 
            4: "Gambling", 5: "Prostitution"}

def run_classification(text): 
    with torch.no_grad(): 
        max_length = 256 
        inputs= tokenizer_1(text, truncation=True, padding=True, max_length = max_length, return_tensors = "pt")
        outputs = torch_script_model_1(inputs["input_ids"])
        logits = outputs["logits"]
        probabilities = logits.softmax(dim = 1)
        predicted_class = torch.argmax(probabilities, dim = 1).item()

    if predicted_class == 1: # If the text is negative 
        # Run model 2 
        with torch.no_grad(): 
            max_length = 256
            inputs = tokenizer_2(text, truncation=True, padding=True, max_length=max_length, return_tensors='pt')
            outputs = torch_script_model_2(inputs["input_ids"])
            logits = outputs["logits"]
            probabilities = logits.softmax(dim=1)
            predicted_class = torch.argmax(probabilities,dim =1).item()
        return id2label[predicted_class]
    else: 
        return "The text is clean" # Clean text 
    

def store_prediction(text,label): 
    ES = ES_DRIVER()
    ES.create(text, label)

