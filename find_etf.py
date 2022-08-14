#### 미국 주식과 우리나라 ETF간 상관 관계를 알아보기 위한 코드
#### 상관 관계는 pearson 방법으로 구함
#### 상관 계수의 범위는 -1 < K < 1 이며 1에 가까울 수록 상관성이 높고 -1에 가까울 수록 상관성이 낮음

import pandas as pd     ####    데이터 가공
import yfinance as yf   ####    야후 파이낸셜
import etf_list as el   ####    종목 코드 리스트

K=0.99      #### 상관 계수 조건

def get_pearson(NORM_TICKER="SPY"):
    el.ETF_LIST.append(NORM_TICKER)
    LIST = el.ETF_LIST
    #### 피어슨 상관계수 구하기 
    #### 기준 자산 ticker 인수 전달
    data = yf.download(LIST)
    data = pd.DataFrame(data['Close'])
    corr = data.corr(method = 'pearson')

    for list in el.ETF_LIST:
        if corr[NORM_TICKER][list] > K :
            print(f"{NORM_TICKER}와 {list}의 상관 계수 : {corr[NORM_TICKER][list]}")

get_pearson("SPY")