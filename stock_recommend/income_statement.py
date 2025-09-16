from search_1 import *
from ratios_filter_logic import *
import json
from datetime import datetime
import datetime

company_list = company_name()
call = CallData()
period = "annual"

#api로 호출한 데이터 저장
for name in company_list:
    income = call.income_statements_api(period, name)
    income_sheet = {name : [] for name in company_list}
    
    file_path = "C:\Users\User\Desktop\그냥 만들기\stock_recommend\data\income_statement_data_sheet.json"
    with open(file_path, 'w') as f:
        json.dump(income_sheet, f)

#netIncome 당기순이익(per 1 year)
def net_income():
    datetime_format = "%Y-%m-%d"
    netincome_surplus = []
    netincome_plus = []
    today = datetime.date.today()
    for key, value in income_sheet:
        netincome = 0
        revenue = 0
        for data in value:
            standard = datetime.strptime(data["date"], datetime_format)
            if today.year - standard.year >= 3:
                netincome += data["netIncome"]
                revenue += data["revenue"]
        netincome_per_year = netincome/len(value)
        revenue_per_year = revenue/len(value)
        np_margin = netincome_per_year/revenue_per_year
        
        if np_margin > 0.05 :
            netincome_surplus.append(key)

    if len(netincome_surplus) ==0 and len(netincome_plus) ==0:
        return "netincome 기준 통과 없음"
    else:
        return netincome_surplus and netincome_plus

#매출이 증가한 회사 리스트, 증가율 반환
def revenue() :
    revenue_list = {}
    for key, value in income_sheet:
        last_year = 1
        growth_rate = []
        for data in value:
            growth_rate.append((data["revenue"]-last_year)/last_year)
            last_year = data["revenue"]

        del growth_rate[0]
        grow = all(num > 0 for num in growth_rate)

        if grow:
            revenue_list[key] = sum(growth_rate)/len(growth_rate)

    return revenue_list