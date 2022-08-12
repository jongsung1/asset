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

def yield_value(ticker="SPY"):
    df_year = fdr.DataReader(ticker,before_one_year) # 12개월 평균 수익률
    YIELD_year = (df_year['Close'][-1] - df_year['Close'][0])/df_year['Close'][0]
    return YIELD_year


YIELD_SPY = yield_value("SPY")
time.sleep(2)
YIELD_EFA = yield_value("EFA")
time.sleep(2)
YIELD_BIL = yield_value("BIL")

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