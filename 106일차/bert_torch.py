import os
import pandas as pd
import numpy as np
import torch
from torch.utils.data import TensorDataset, DataLoader
from torch.optim.lr_scheduler import StepLR
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# Load the dataset
whole_data = pd.read_csv('train.csv', encoding='utf-8')
data_train, data_valid = train_test_split(whole_data, test_size=0.1, random_state=99)

# Define the device to use for training
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2).to(device)

# Tokenize the input text and convert to PyTorch tensors
X_train = [tokenizer.encode(text, add_special_tokens=True, max_length=350, truncation=True, padding='max_length')
           for text in data_train['text'].tolist()]
X_train = torch.tensor(X_train, dtype=torch.long).to(device)
y_train = torch.tensor(data_train['target'].tolist(), dtype=torch.long).to(device)

X_test = [tokenizer.encode(text, add_special_tokens=True, max_length=350, truncation=True, padding='max_length')
          for text in data_valid['text'].tolist()]

X_test = torch.tensor(X_test, dtype=torch.long).to(device)
y_test = torch.tensor(data_valid['target'].tolist(), dtype=torch.long).to(device)

# Create a PyTorch dataset and data loader
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Define the optimizer and loss function
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-7)
loss_fn = torch.nn.CrossEntropyLoss().to(device)
# scheduler = StepLR(optimizer, step_size=10, gamma=0.1)
# Reduce learning rate by a factor of 0.1 after every 10 epochs
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.2, patience=2, verbose=True)

# Train the model
for epoch in range(100):
    model.train()
    total_loss = 0
    for batch in tqdm(train_loader, desc=f"Training epoch {epoch+1}"):
        optimizer.zero_grad()
        input_ids, labels = batch
        outputs = model(input_ids, labels=labels)
        loss = loss_fn(outputs[1], labels)
        total_loss += loss.item()
        loss.backward()
        optimizer.step()
        # scheduler.step()  # stepLR scheduler
    avg_loss = total_loss / len(train_loader)
    print(f"\nAverage loss for epoch {epoch+1}: {avg_loss:.6f}")
    # print(f"Current learning rate: {optimizer.param_groups[0]['lr']}")

    # Evaluate the model on the validation set
    model.eval()
    with torch.no_grad():
        y_pred = []
        for batch in tqdm(zip(X_test.split(32), y_test.split(32)), desc="Evaluating"):
            input_ids, labels = batch
            outputs = model(input_ids)
            y_pred += outputs[0].argmax(axis=1).tolist()
        accuracy = np.mean(np.array(y_pred) == y_test.cpu().numpy())
        print(f"Validation accuracy: {accuracy:.4f}")
        scheduler.step(avg_loss)

        # Save the model
        os.makedirs('D:/models', exist_ok=True)
        torch.save(model.state_dict(), f"D:/models/bert_model_epoch{epoch+1}.pth")
