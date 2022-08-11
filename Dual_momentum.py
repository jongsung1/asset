from calendar import day_abbr
import FinanceDataReader as fdr
from matplotlib.pyplot import close
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
print("현재 :" , now)	# 현재 : 2021-01-09 20:07:09.682594

before_one_day = now - relativedelta(days=1)
print("1일 전 :", before_one_day)	# 1일 전 : 2021-01-08 20:07:09.682594

before_one_year = now - relativedelta(years=1)
print("1년 전 :", before_one_year)	# 1년 전 : 2020-01-09 20:07:09.682594

df = fdr.DataReader('KR1YT=RR',before_one_year) # 1년만기 한국국채 수익률
print(df['Close'])

print(df['Close'][0])   ### 1년 전 종가
print(df['Close'][-1])  ### 현재가