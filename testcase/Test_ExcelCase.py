from config.conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Requests
import pytest

case_file = os.path.join("../data" , ConfigYaml().get_excel_file())
sheet_name = ConfigYaml().get_excel_sheet()

data_init = Data(case_file , sheet_name)
run_list = data_init.get_run_data()

log = my_log()
data_key = ExcelConfig.DataConfig
class TestExcel:
    def run_api(self,url,method,params=None,headers=None,cookies=None):
        if len(str(params).strip()) == 0 :
            headers = eval(headers)
        if len(str(headers).strip()) == 0 :
            params = eval(params)
        request = Requests()
        if str(method).lower() == "get":
            res = request.get(url, json=params, headers=headers)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=headers)
        else:
            log.error("这是一个错误的method: %s" % method)
        return res




    def run_pre(self,pre_case):
        #初始化数据
        url = "http://" + ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        expect_result = pre_case[data_key.expect_result]
        res = self.run_api(url,method,params,headers)
        print(res)



    @pytest.mark.parametrize("case",run_list)
    def test_run(self,case):

        url = "http://" + ConfigYaml().get_conf_url()+ case[data_key.url]
        case_id = case[data_key.case_id]
        case_module = case[data_key.case_module]
        api_name = case[data_key.api_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        para_type = case[data_key.para_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        actual_result = case[data_key.actual_result]
        remark = case[data_key.remark]
        is_run = case[data_key.is_run]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        status_code = case[data_key.status_code]
        db_assert = case[data_key.db_assert]
        if len(str(params).strip()) == 0 :
            headers = eval(headers)
        if len(str(headers).strip()) == 0 :
            params = eval(params)

        if pre_exec:
            pass
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件为： %s"%pre_case)
            self.run_pre(pre_case)

        request = Requests()
        if str(method).lower() == "get" :
            res =request.get(url,json=params,headers=headers)
        elif str(method).lower() == "post":
            res = request.post(url,json=params,headers=headers)
        else:
            log.error("这是一个错误的method: %s"%method)
        print(res)

#TestExcel().test_run()
if __name__ == "__main__":
    pytest.main(["-s","Test_ExcelCase.py"])