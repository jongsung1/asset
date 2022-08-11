from fredapi import Fred
fred = Fred(api_key='dfe675cece937fd821d496302a879d8b')

### S&P500 이동평균
SPY="S&P500"
SPY_MOVING=200

SPY_DATA = fred.get_series('SP500')
SPY_END=SPY_DATA.size-1 ## 사이즈 크기 -1
SPY_START=SPY_END-220   ## nan 제거 하기위해 20 추가

#### 실업률
UNRATE="미국 실업률"
UNRATE_MOVING=12

UNRATE_DATA = fred.get_series('UNRATE')
UNRATE_END=UNRATE_DATA.size-1 ## 사이즈 크기 -1
UNRATE_START=UNRATE_END-220   ## nan 제거 하기위해 20 추가

flag=0
SUM=0

def moving_avarage(end, start, data,flag=0,SUM=0,moving="200"):
    for i in range(end, start, -1):
        if flag < moving :
            if data[i] > 0 :
                # print(data[i])
                SUM=data[i]+SUM
                flag = flag + 1
    return SUM/moving

SPY_MOVING_AVARAGE=moving_avarage(SPY_END,SPY_START,SPY_DATA,flag,SUM,SPY_MOVING)
UNRATE_MOVING_AVARAGE=moving_avarage(UNRATE_END,UNRATE_START,UNRATE_DATA,flag,SUM,UNRATE_MOVING)

DIFF_SPY = SPY_DATA[SPY_END] - SPY_MOVING_AVARAGE   ### S&P500 현재가와 200일 이동평균 차이
DIFF_UNRATE = UNRATE_DATA[UNRATE_END] - UNRATE_MOVING_AVARAGE   ### 미국 실업률 현재가와 12개월 이동평균 차이

print("%s %s 일 이동평균 : %s" % (SPY,SPY_MOVING,SPY_MOVING_AVARAGE))
print("%s 현재가 : %s" % (SPY,SPY_DATA[SPY_END]))
print("%s %s 개월 이동평균 : %s" % (UNRATE,UNRATE_MOVING,UNRATE_MOVING_AVARAGE))
print("%s 현재가 : %s" % (UNRATE,UNRATE_DATA[UNRATE_END]))


if DIFF_SPY < 0 and DIFF_UNRATE > 0 :
    print("buy SHY")
else :
    print("buy QQQ")
