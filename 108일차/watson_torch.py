import numpy as np
import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
from torch.utils.data import TensorDataset, DataLoader

train = pd.read_csv("train.csv")

model_name = 'bert-base-multilingual-cased'
tokenizer = BertTokenizer.from_pretrained(model_name)
max_len = 50


def encode_sentence(s):
    tokens = list(tokenizer.tokenize(s))
    tokens.append('[SEP]')
    if len(tokens) > max_len:
        tokens = tokens[:max_len - 1] + ['[SEP]']

    return tokenizer.convert_tokens_to_ids(tokens)


def bert_encode(hypotheses, premises, tokenizer):
    num_examples = len(hypotheses)

    sentence1 = [encode_sentence(s) for s in np.array(hypotheses)]
    sentence1 = torch.tensor(sentence1)

    sentence2 = [encode_sentence(s) for s in np.array(premises)]
    sentence2 = torch.tensor(sentence2)

    cls = [tokenizer.convert_tokens_to_ids(['[CLS]'])] * sentence1.shape[0]
    cls = torch.tensor(cls)

    input_word_ids = torch.cat([cls, sentence1, sentence2], dim=-1)
    input_word_ids = torch.nn.functional.pad(input_word_ids, (0, max_len - input_word_ids.shape[-1]), mode='constant', value=0)

    input_mask = torch.ones_like(input_word_ids)

    type_cls = torch.zeros_like(cls)
    type_s1 = torch.zeros_like(sentence1)
    type_s2 = torch.ones_like(sentence2)
    input_type_ids = torch.cat([type_cls, type_s1, type_s2], dim=-1)
    input_type_ids = torch.nn.functional.pad(input_type_ids, (0, max_len - input_type_ids.shape[-1]), mode='constant', value=0)

    inputs = {
        'input_word_ids': input_word_ids,
        'input_mask': input_mask,
        'input_type_ids': input_type_ids}

    return inputs


train_dataset = bert_encode(train.hypothesis.values, train.premise.values, tokenizer)
batch_size = 64
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = BertModel.from_pretrained(model_name)
model.to(device)


def predict(model, dataloader):
    model.eval()
    predictions = []
    with torch.no_grad():
        for batch in dataloader:
            batch = tuple(t.to(device) for t in batch)
            input_ids, attention_mask, token_type_ids = batch
            outputs = model(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
            pooled_output = outputs[1]
            _, prediction = torch.max(pooled_output, dim=1)
            predictions.extend(prediction.cpu().numpy())

    return predictions


num_epochs = 2
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)

for epoch in range(num_epochs):
    running_loss = 0.0
    for step, batch in enumerate(train_dataloader):
        batch = tuple(t.to(device) for t in batch)
        input_ids, attention_mask, token_type_ids = batch
        labels = torch.tensor(train.label.values[step*batch_size:(step+1)*batch_size]).to(device)
        model.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        pooled_output = outputs[1]
        loss = torch.nn.functional.cross_entropy(pooled_output, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    epoch_loss = running_loss / len(train_dataloader)
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, epoch_loss))

test = pd.read_csv("test.csv")
test_dataset = bert_encode(test.hypothesis.values, test.premise.values, tokenizer, max_len=50)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

predictions = predict(model, test_dataloader)

submission = pd.DataFrame({'id': test.id, 'prediction': predictions})
submission.to_csv('submission.csv', index=False)
