#### 미국 주식과 우리나라 ETF간 상관 관계를 알아보기 위한 코드
#### 상관 관계는 pearson 방법으로 구함
#### 상관 계수의 범위는 -1 < K < 1 이며 1에 가까울 수록 상관성이 높고 -1에 가까울 수록 상관성이 낮음

import pandas as pd     ####    데이터 가공
import yfinance as yf   ####    야후 파이낸셜
import etf_list as el   ####    종목 코드 리스트
from tqdm import tqdm   ####### 진행률 표시 - for문에 사용

K=0.99      #### 상관 계수 조건
ETF={}      #### 상관 계수 조건 맞는 ETF 담을 딕셔너리

#### 피어슨 상관계수 구하기 
#### 기준 자산 ticker 인수 전달
def get_pearson(ticker="SPY"):
    for list in tqdm(el.ETF_LIST):
        data = yf.download([ticker,list])
        data = pd.DataFrame(data['Close'])
        corr = data.corr(method = 'pearson')
        #### 상관 계수 조건(K)에 맞으면 ETF 딕셔너리에 저장 ==> 한번에 출력하기 위함
        if corr[ticker][list] > K :
            ETF[list] = corr[ticker][list]
    
    #### 상관 계수 리스트 출력
    print("결과 : %s" % (len(ETF)))
    for key in ETF:
        print(f"{ticker}와 {key}의 상관 계수 : {ETF[key]}")

get_pearson("SPY")