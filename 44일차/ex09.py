# 시간대 변경하기
import pandas as pd
import pytz
from pytz import all_timezones

# date = pd.Timestamp('2022-12-05 01:40:00') # dateitem 생성
#
# date_in_london = date.tz_localize(tz='Europe/London')
# print(date_in_london)
#
# date_in_abidjan = date_in_london.tz_convert('Africa/Abidjan')
#
dates = pd.Series(pd.date_range('2/2/2022', periods=3, freq='M'))
# temp = dates.dt.tz_localize('Africa/abidjan')
#
# print(temp)

# print(all_timezones[0:2])
temp = dates.dt.tz_localize('dateutil/Asia/Seoul')
tz = pytz.timezone('Asia/Seoul')
temp01 = dates.dt.tz_localize(tz)
print(temp01)
