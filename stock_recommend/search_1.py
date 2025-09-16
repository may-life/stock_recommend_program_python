import requests
import face_recognition



# def general_search_API(whether_endpoint, user_finds) :
#     '''
#     암호화폐, 외환, 주식, ETF, 기타 금융 상품등을 symbol/name/회사이름 으로 검색
#     '''

#     url_common_front = "https://financialmodelingprep.com/api/v3/search?"
#     url_api_already_endpoint = "&apikey="
#     url_api_without_endpoint = "?apikey="
#     appid = "jMfAke0oNKyGdWiseV77TCpUqrOmjtwB"
#     url = ''


#     if whether_endpoint == True:
#         url = url_common_front + url_api_already_endpoint + appid
#     else:
#         url = url_common_front + url_api_without_endpoint + appid
    
#     json_data = requests.get(url).json()

#     for i in range(len(json_data)):
#         if user_finds == json_data[i]["symbol"]:
#             target_data = json_data[i]
#             for key, value in target_data.items():
#                 return f"{key} : {value}"
            
#         elif user_finds == json_data[i]["name"]:
#             target_data = json_data[i]
#             for key, value in target_data.items():
#                 return f"{key} : {value}"
            
#         elif user_finds == json_data[i]["exchangeShortName"]:
#             target_data = json_data[i]
#             for key, value in target_data.items():
#                 return f"{key} : {value}"


# def company_profile_api():
#     '''
#     포괄적 개요(가격, 베타, 시총, 설명, 본사 등의 정보)제공
#     '''

#     url_front = "https://financialmodelingprep.com/api/v3/profile/"
#     endpoint = "AAPL"
#     api_id = "jMfAke0oNKyGdWiseV77TCpUqrOmjtwB"
#     url_api_already_endpoint = "&apikey="

#     url = url_front + endpoint + url_api_already_endpoint + api_id

#     json_data = requests.get(url).json()


class Screener_stock:
    '''
    사용자가 설정한 범위의 31개 종목 추려내기(무료버전)
    '''
    def __init__(self):
        pass
    
    def screener_stock_api(self, user_stock_higher_than, user_stock_lower_than):
        url_front = "https://financialmodelingprep.com/api/v3/stock-screener?"
        url_market_cap_more_than = "marketCapMoreThan="
        url_market_cap_lower_than = "&marketCapLowerThan="
        url_return_on_equity_more_than = "&returnOnEquityMoreThan=15" #roe 15%이상
        url_pe_lower_than = "&peLowerThan=15"  #per 15이하
        url_price_to_book_ratio_lower_than = "&priceToBookRatioLowerThan=1.5" #pbr 1.5이하
        url_limit = "&limit=31"
        url_apikey = "jMfAke0oNKyGdWiseV77TCpUqrOmjtwB"

        url = url_front + url_market_cap_more_than + user_stock_higher_than + url_market_cap_lower_than + user_stock_lower_than + url_return_on_equity_more_than + url_pe_lower_than + url_price_to_book_ratio_lower_than + url_limit + url_apikey

        filtered_json_data = requests.get(url).json()
        
        return filtered_json_data

class CallData:

    def __init__(self):
        self.url_front = "https://financialmodelingprep.com/api/v3/"
        self.profile = "profile/"
        self.income_statement = "income-statement/"
        self.balance_sheet = "balance-sheet-statement/"
        self.cash_flow = "cash-flow-statement/"
        self.ratios = "ratios/AAPL?"
        self.historical_price = "historical-price-full/"
        self.stock_dividend = "historical/stock_dividend/"
        self.url_api_already_endpoint = "&apikey="
        self.url_api_without_endpoint = "?apikey="
        self.appid = "jMfAke0oNKyGdWiseV77TCpUqrOmjtwB"

    
    def company_profile_api(self, user_finds):
        url = self.url_front + user_finds + "?" + self.profile + self.url_api_already_endpoint + self.appid
        profile_json_data = requests.get(url).json()
        return profile_json_data
    

    def income_statements_api(self, period, user_finds): #annual/quater
        if period == "annual" :
            url = self.url_front  + user_finds + "?" + self.income_statement + "period=annual" + self.url_api_already_endpoint + self.appid
        elif period == "quarter":
            url = self.url_front  + user_finds + "?" + self.income_statement + "period=quarter" + self.url_api_already_endpoint + self.appid

        profile_json_data = requests.get(url).json()
        return profile_json_data
    
    
    def balance_sheet_api(self, period, user_finds):
        if period == "annual" :
            url = self.url_front  + user_finds + "?" + self.balance_sheet + "period=annual" + self.url_api_already_endpoint + self.appid

        elif period == "quarter":
            url = self.url_front  + user_finds + "?" + self.balance_sheet + "period=quarter" + self.url_api_already_endpoint + self.appid

        profile_json_data = requests.get(url).json()
        return profile_json_data
    
    
    def cash_flow_api(self, period, user_finds):
        if period == "annual" :
            url = self.url_front  + user_finds + "?" + self.cash_flow + "period=annual" + self.url_api_already_endpoint + self.appid

        elif period == "quarter":
            url = self.url_front  + user_finds + "?" + self.cash_flow + "period=quarter" + self.url_api_already_endpoint + self.appid

        profile_json_data = requests.get(url).json()
        return profile_json_data
    
    
    def ratios_api(self, period, user_finds):
        if period == "annual" :
            url = self.url_front  + user_finds + "?" + self.ratios + "period=annual" + self.url_api_already_endpoint + self.appid

        elif period == "quarter":
            url = self.url_front  + user_finds + "?" + self.ratios + "period=quarter" + self.url_api_already_endpoint + self.appid

        profile_json_data = requests.get(url).json()
        return profile_json_data
    
    
    def historical_price_api(self, user_finds):
        url = self.url_front + user_finds + self.historical_price + self.url_api_already_endpoint + self.appid
        profile_json_data = requests.get(url).json()
        return profile_json_data
    
    
    def stock_divinded_api(self, user_finds):
        url = self.url_front  + user_finds + self.historical_price + self.url_api_already_endpoint + self.appid
        profile_json_data = requests.get(url).json()
        return profile_json_data