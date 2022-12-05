import pandas as pd
import numpy as np

time_index = pd.date_range('01/01/2022', periods=5, freq='M')
dataframe = pd.DataFrame(index=time_index)  # 데이터 프레임 생성 및 인덱스 지정
# print(dataframe)

dataframe['Sales'] = [1.0, 2.0, np.nan, np.nan, 5.0]    # 누락된 값이 있는 특성 생성
data00 = dataframe.interpolate()  # 누락값 보간
dataf = dataframe.ffill()    # 앞쪽 값을 기준으로 보간
datab = dataframe.bfill()    # 뒷쪽 값을 기준으로 보간
# print(data00)
# print(dataf)
# print(datab)

datanl = dataframe.interpolate(method='quadratic')
# print(datanl)
# 보간 방향 지정
datafw = dataframe.interpolate(limit=1, limit_direction='forward')
print(datafw)