from search_1 import *

user_period = input("annual/quarter 중 하나를 입력해주십시오 : ")
#ROE 비율 확인
call_data1 = CallData()
ratio_data_set = call_data1.ratios_api(user_period)
roe_over_15 = []
for i in range(len(ratio_data_set)):
    if ratio_data_set[i]["returnOnEquity"] >= 0.15 :
        roe_over_15.append(ratio_data_set[i])

# 부채비율(Debt/Equity) < 1
"""ratios 비율이 fmp에서 막혀서 사용불가"""
debt_equity_rate = []
for i in range(len(ratio_data_set)):
    if ratio_data_set[i]["debtEquityRatioTTM"] < 1:
        debt_equity_rate.append(ratio_data_set[i])

# screener stock로 1차 필터링
