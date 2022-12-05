import pandas as pd

dataframe = pd.DataFrame()
dataframe['date'] = pd.date_range('1/1/2022', periods=150, freq='w')

# 년 월 일 시 분에 대한 특성을 생성
data_year = dataframe['year'] = dataframe['date'].dt.year
data_month = dataframe['month'] = dataframe['date'].dt.month
data_day = dataframe['day'] = dataframe['date'].dt.day
data_hour = dataframe['hour'] = dataframe['date'].dt.hour
data_minute = dataframe['minute'] = dataframe['date'].dt.minute

print(dataframe.head())