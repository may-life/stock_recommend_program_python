from search_1 import *

#filtered data에서 회사명만 추출하기
user_stock_lower_than = int(input("찾고자하는 종목의 시총 최대치를 입력하세요 : "))
user_stock_higher_than = int(input("찾고자하는 종목의 시총 최저치를 입력하세요 : "))

stock_screener_data_set = ScreenerStock().screener_stock_api(user_stock_higher_than, user_stock_lower_than)

company_name_list = []

for i in range(len(stock_screener_data_set)):
    company_name_list.append(stock_screener_data_set[i]["companyName"])

call = CallData()

#ratios api 받기
ratios_data_set = []
period = "annual"
for name in company_name_list:
    data = call.ratios_api(period, name)
    data["companyName"] = name
    ratios_data_set.append(data)

#영업이익률(operatingProfitMarginTTM) > 15%, TTM => 12months
opm_list = []

for i in range(len(ratios_data_set)):
    if ratios_data_set[i]["operationProfitMarginTTM"] > 0.15:
        opm_list.append(ratios_data_set[i])

#순이익률(netProfitMarginTTM) > 10%
npfm_list = []

for i in range(len(ratios_data_set)):
    if ratios_data_set[i]["netProfitMarginTTM"] > 0.1:
        npfm_list.append(ratios_data_set[i])

#이자보상배율(interestCoverageTTM) > 5
ic_list = []

for i in range(len(ratios_data_set)):
    if ratios_data_set[i]["interestCoverageTTM"] > 5:
        ic_list.append(ratios_data_set[i])

#P/FCF < 15
p_fcf_list = []

for i in range(len(ratios_data_set)):
    if ratios_data_set[i]["priceToFreeCashFlowsRatioTTM"] < 15:
        npfm_list.append(ratios_data_set[i])

def scanner_data():
    return stock_screener_data_set

def company_name():
    return company_name_list

def ratios_data():
    return ratios_data_set


def ratios_filter():
    first_confirm = []
    second_confirm = []
    third_confirm = []
    final_confirm = []
    for confirm_ratios in ratios_data_set:
        for confirm_opm in opm_list:
            if confirm_ratios["companyName"] == confirm_opm["companyName"]:
                first_confirm.append(confirm_opm)
                break

    for confirm_npfm in npfm_list:
        for confirm_ic in ic_list:
            if confirm_npfm["companyName"] == confirm_ic["companyName"]:
                second_confirm.append(confirm_ic)
                break
    
    for confirm_npfm in first_confirm:
        for confirm_ic in second_confirm:
            if confirm_npfm["companyName"] == confirm_ic["companyName"]:
                third_confirm.append(confirm_ic)
                break
    for final in third_confirm:
        for confirm_fcf in p_fcf_list:
            if final["companyName"] == confirm_fcf["companyName"]:
                final_confirm.append(confirm_fcf)
    if len(final_confirm) == 0:
        return "조건에 부합한 주식을 찾지 못했습니다"
    else:
        return final_confirm