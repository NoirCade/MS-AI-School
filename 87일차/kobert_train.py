import pandas as pd
from sklearn.preprocessing import LabelEncoder
import torch
from kobert import get_pytorch_kobert_model

dataset_train = pd.read_csv('./stock_list_train.csv')
name_data = pd.read_csv('./stock_name_list.csv')
new_df = dataset_train

# for i in range(len(new_df)):
#     new_df['종목명'][i] = name_data['전체 종목명'].iloc[dataset_label[i]]

encoder = LabelEncoder()
encoder.fit(dataset_train['라벨명'])
dataset_train['라벨명'] = encoder.transform(dataset_train['라벨명'])

mapping = dict(zip(range(len(encoder.classes_)), name_data['전체 종목명']))
# mapping = {0: 'CJ대한통운', 1: '유한양행', 2: '대한항공', 3: '현대자동차', 4: 'NH투자증권', 5: 'SK텔레콤'}


