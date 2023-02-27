import pandas as pd

label = pd.read_csv('./train_labels.csv')
df = pd.read_csv('./train.csv')

sess_list = df.session_id.unique()
mi_list = []

print(df[])
exit()
for i in sess_list:
    df[i]
    mi_list.append(df.session_id)

# print(len(sess_list))