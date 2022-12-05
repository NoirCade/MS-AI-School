import numpy as np
import pandas as pd

data_strings = np.array(['12-05-2022 01:28 PM',
                         '12-06-2022 02:28 PM',
                         '12-07-2022 12:00 AM'])
# Timestamp
for data in data_strings:
    data = pd.to_datetime(data, format='%d-%m-%Y %I:%M %p')
    print(data)


for data in data_strings:
    data = pd.to_datetime(data, format='%d-%m %I:%M %p', errors="ignore")
    # 데이터 포맷에 에러가 있더라도 무시하고 그냥 출력해줌(Y나 m 부분 등을 누락하더라도 알아서 출력해줌)
    print(data)