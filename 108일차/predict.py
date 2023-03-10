import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the saved model
model_path = './submit/bert_model_good_0_0.8461.pt'
model_state_dict = torch.load(model_path)
tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased')
model = AutoModelForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=len(LABELS))
model.load_state_dict(model_state_dict)

# Put the model in evaluation mode
model.eval()

# Tokenize the input text
text = "The earth revolves around the sun."
encoding = tokenizer(text, padding='max_length', truncation=True, max_length=128, return_tensors='pt')

# Convert the tokenized input into PyTorch tensors and move them to device
input_ids = encoding['input_ids'].to(device)
attention_mask = encoding['attention_mask'].to(device)
token_type_ids = encoding['token_type_ids'].to(device)

# Make prediction
with torch.no_grad():
    output = model(input_ids, attention_mask, token_type_ids, return_dict=True)
    logits = output.logits
    predicted_label = torch.argmax(logits, dim=1).item()

# Map the predicted label index to the corresponding label string
predicted_label_str = LABELS[predicted_label]
print(predicted_label_str)