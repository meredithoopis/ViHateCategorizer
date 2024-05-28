from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

# Get the current working directory
current_dir = os.getcwd()

# Model and tokenizer loading: Checking if a toxic comment belongs to a particular category

''' 
# Uncomment this section to use a locally saved TorchScript model and tokenizer: Can be found on the Google Drive link on the README.md file
# torch_script_model = torch.jit.load(os.path.join(current_dir, "models/6_classes/tokenizer/Model_6.pt"))
# torch_script_model.eval()
# tokenizer = AutoTokenizer.from_pretrained(os.path.join(current_dir, "models/6_classes/tokenizer/torchscript_model"))
'''

# Pretrained model name
model_name = "lisagrace/hate_speech_bert"

# Load tokenizer and model from the pretrained model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Mapping from class ID to label
id2label = {0: "Reactionary", 1: "Hate and violence", 2: "Discrimination", 3: "Self-harm", 
            4: "Gambling", 5: "Prostitution"}

def run_classification(text) -> str:
    """
    Runs classification on the given text to determine its toxicity category.
    
    Args:
        text (str): The input text to classify.
    
    Returns:
        str: The predicted category label for the input text.
    """
    with torch.no_grad():
        max_length = 256
        inputs = tokenizer(text, truncation=True, padding=True, max_length=max_length, return_tensors="pt")
        outputs = model(inputs["input_ids"])
        logits = outputs["logits"]
        probabilities = logits.softmax(dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
    return id2label[predicted_class]

# Example usage of the run_classification function
# label = run_classification("Tao đánh chết cha mày giờ")
# print(label)
