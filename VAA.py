from calendar import day_abbr
import FinanceDataReader as fdr
from matplotlib.pyplot import close
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time ### HTTP 429 error 에러 발생으로 자료 조회 후 time sleep 

now = datetime.now()    ## 현재
before_one_day = now - relativedelta(days=1)        ## 하루 전
before_one_month = now - relativedelta(months=1)    ## 1달 전
before_three_month = now - relativedelta(months=3)  ## 3달 전
before_six_month = now - relativedelta(months=6)    ## 6달 전
before_one_year = now - relativedelta(years=1)      ## 1년 전

def score(ticker="SPY"):
    df_one_month = fdr.DataReader(ticker,before_one_month) # 미국 주식(SPY) 1개월 평균 수익률
    time.sleep(1.8)
    df_three_month = fdr.DataReader(ticker,before_three_month) # 미국 주식(SPY) 3개월 평균 수익률
    time.sleep(1.8)
    df_six_month = fdr.DataReader(ticker,before_six_month) # 미국 주식(SPY) 6개월 평균 수익률
    time.sleep(1.8)
    df_year = fdr.DataReader(ticker,before_one_year) # 미국 주식(SPY) 12개월 평균 수익률

    YIELD_one_month = (df_one_month['Close'][-1] - df_one_month['Close'][0])/df_one_month['Close'][0]
    YIELD_three_month = (df_three_month['Close'][-1] - df_three_month['Close'][0])/df_three_month['Close'][0]
    YIELD_six_month = (df_six_month['Close'][-1] - df_six_month['Close'][0])/df_six_month['Close'][0]
    YIELD_year = (df_year['Close'][-1] - df_year['Close'][0])/df_year['Close'][0]

    SCORE = 12*YIELD_one_month + 4*YIELD_three_month + 2*YIELD_six_month + YIELD_year

    return SCORE


SCORE_SPY = score("SPY")
SCORE_EFA = score("EFA")
SCORE_EEM = score("EEM")
SCORE_AGG = score("AGG")
SCORE_LQD = score("LQD")
SCORE_IEF = score("IEF")
SCORE_SHY = score("SHY")

