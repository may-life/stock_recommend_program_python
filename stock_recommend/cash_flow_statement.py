from income_statement import *
from ratios_filter_logic import company_name
from search_1 import *

call = CallData()
revenue_list = revenue()
company_list = company_name()
period = "annual"
cash_flow_dict = {}

#cash_flow_statement 호출, extra : 저장기능 추가?
for name in company_list:
    cash_flow = call.cash_flow_api(period, name)
    cash_flow_dict[f"{name}"] = cash_flow 

class CashFlow:
    '''cash_flow_statement 관련 연산 수행'''

    def __init__(self):
        self.data = None

    def load_data(self):
        if self.data == None:
            self.data = self.get_info()
        return self.data
    
    def refresh_data(self):
        self.data = self.get_info()

    #{name : {'name_1' :{ocf, capex, }, 'name_2' : {}}}
    def get_info(self):

        result = {}

        for key, value in cash_flow_dict.items():
            info_dict = {}
            ocf_list = []
            capex_list = []
            fcf_list = []

            for data in value:
                ocf_list.append(data["operatingCashFlow"])
                capex_list.append(data["capitalExpenditure"])
                fcf_list.append(data["freeCashFlow"])

            info_dict["ocf"] = ocf_list
            info_dict["capex"] = capex_list
            info_dict["fcf"]=fcf_list

            result[key] = info_dict
        
        return result

    # return  ==>  기준 통과 회사이름 리스트, ocf평균치 딕셔너리 
    def ocf_logic(self) :
        data_set = self.load_data()
        pass_name_list = []
        ocf_avg_dict = {}
        for key, value in data_set.items():
            ocf_data = sum(value["ocf"])
            
            if ocf_data > 0:
                pass_name_list.append(key)
                ocf_avg_dict[f"{name}"] = ocf_data
        return pass_name_list and ocf_avg_dict
    
    def capex_logic(self, min = 0.3, max = 0.5):
        data_set = self.load_data()
        ocf_name, ocf_avg_dict = self.ocf_logic()
        
        capex_avg_dict = {}
        for key, value in data_set.items():
            capex_sum = 0
            for data in value:
                capex_sum += data["capitalExpenditure"]

        return [
            k for k in capex_avg_dict 
            if k in ocf_avg_dict and 
            ocf_avg_dict[k]*min >= capex_avg_dict[k]
        ]