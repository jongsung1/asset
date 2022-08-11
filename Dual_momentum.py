from calendar import day_abbr
import FinanceDataReader as fdr
from matplotlib.pyplot import close
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time ### HTTP 429 error 에러 발생으로 자료 조회 후 time sleep 

now = datetime.now()    ## 현재
before_one_day = now - relativedelta(days=1)        ## 하루 전
before_one_year = now - relativedelta(years=1)      ## 1년 전
before_one_month = now - relativedelta(months=1)    ## 1달 전

df_year_SPY = fdr.DataReader('SPY',before_one_year) # 미국 주식(SPY) 12개월 평균 수익률
YIELD_SPY = (df_year_SPY['Close'][-1] - df_year_SPY['Close'][0])/df_year_SPY['Close'][0]
time.sleep(1.8)

df_year_EFA = fdr.DataReader('EFA',before_one_year) # 선진국 주식(EFA) 12개월 평균 수익률
YIELD_EFA = (df_year_EFA['Close'][-1] - df_year_EFA['Close'][0])/df_year_EFA['Close'][0]
time.sleep(1.8)

df_year_BIL = fdr.DataReader('BIL',before_one_year) # 초단기채권(BIL) 12개월 평균 수익률
YIELD_BIL = (df_year_BIL['Close'][-1] - df_year_BIL['Close'][0])/df_year_BIL['Close'][0]

print("SPY 수익률 : %s" % (YIELD_SPY))
print("EFA 수익률 : %s" % (YIELD_EFA))
print("BIL 수익률 : %s" % (YIELD_BIL))

if YIELD_SPY < YIELD_BIL :
    print("buy AGG 100%")
else :
    if YIELD_SPY > YIELD_EFA :
        print("buy SPY 100%")
    else :
        print("buy EFA 100%")
