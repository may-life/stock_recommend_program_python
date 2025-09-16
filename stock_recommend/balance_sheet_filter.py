from search_1 import *
from ratios_filter_logic import *

call = CallData()

company_list = company_name()
stock_screener_data_set
period = "annual"

#balance-sheet-statement 호출
balance_sheet = {name : [] for name in company_list}


for name in company_list:
    balance = call.balance_sheet_api(period, name)
    balance_sheet[f"{name}"] = balance


    
#자산 > 부채
def debt_enough(): 
    debt_ok_list = []
    check_need = []
    for key, value in balance_sheet.items():
        fail_num = 0
        for data in value:
            if data["totalAssets"] <= data["totalLiabilities"]:
                fail_num += 1
        if fail_num == 0:
            debt_ok_list.append(key)
        elif fail_num ==1:
            check_need.append(key)
    return debt_ok_list and check_need



#자기자본 증가 추세
def total_equity():
    equity_ok_list = []
    equity_review_needed = []


    for key, value in balance_sheet:
        tendency_list = []
        fail = 0
        review_need = 0

        for i in range(len(value)-1):
            late = value[i]["totalStockholdersEquity"]
            early = value[i+1]["totalStockholdersEquity"]
            tendency = (late - early)/early
            if tendency < -0.05:
                fail += 1
            elif tendency > -0.05 and tendency < 0:
                review_need += 1
        
        if fail != 0 and review_need ==0:
            equity_ok_list.append(key)
        elif fail != 0 and review_need != 0:
            equity_review_needed.append(key)
    return equity_ok_list and equity_review_needed
        

def cash_ratio():
    stable = []
    normal = []
    danger = []

    for key, value in balance_sheet.items():
        cash_years = []
        for data in value:
            cash = data["cashAndCashEquivalents"]
            cl = data["totalCurrentLiabilities"]
            cash_ratio = cash/cl
            cash_years.append(cash_ratio)
        total = sum(cash_years)
        tendency = total/len(value)
        
        if tendency >= 1.0:
            stable.append(key)
        elif tendency >= 0.3:
            normal.append(key)
        elif tendency <= 0.2:
            danger.append(key)
    return stable and normal and danger

