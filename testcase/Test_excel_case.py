import re

from config.conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from common import Base
from utils.RequestsUtil import Requests
import pytest
import json
#初始化用例文件
case_file = os.path.join("../data",ConfigYaml().get_excel_file())
#初始化sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
#获取运行测试用例列表
data_init = Data(case_file,sheet_name)
run_list = data_init.get_run_data()

#获取日志
log = my_log()
#测试用例方法，参数化运行
#初始化data_config
data_key = ExcelConfig.DataConfig
class TestExcel:
    def run_pre(self,pre_case):
        #初始化数据
        url = "http://" + ConfigYaml().get_conf_url() + pre_case[data_key.url]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        method = pre_case[data_key.method]
        if len(str(headers)) == 0:
            params = eval(params)
        if len(str(params)) == 0:
            headers =eval(headers)
        request = Requests()
        if str(method).lower() == "post":
            res = request.post(url, json=params)
        elif str(method).lower() == "get":
            res = request.get(url, headers=headers)
        else:
            log.error("错误method: %s" % method)
        print("前置用例执行： %s"%res)
        return  res

    #pytest
    #方法修改
    #重构函数内容
    #pytest.main 运行
    @pytest.mark.parametrize("case",run_list)
    def test_run(self,case):
        #data_key = ExcelConfig.DataConfig
        #run_list第一个用例，通过Key获取value值,[i]从执行的case里面进行，0开始
        url = "http://" + ConfigYaml().get_conf_url() + case[data_key.url]
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
        # if len(str(headers)) == 0:
        #     params = eval(params)
        # if len(str(params)) == 0:
        #     headers =eval(headers)

        # 验证前置条件
        if pre_exec:
            pass
            # 找到执行用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件信息：%s"%pre_case)
            pre_res = self.run_pre(pre_case)
            headers,cookies = self.get_correlation(headers,cookies,pre_res)
        if len(str(headers)) == 0:
            params = eval(params)
        if len(str(params)) == 0:
            headers = eval(headers)

        request = Requests()
        if str(method).lower() == "post":
            res = request.post(url,json = params)
        elif str(method).lower() == "get":
            res = request.get(url, headers = headers)
        else:
            log.error("错误method: %s"%method)
        print("测试用例执行： %s" % res)

def get_correlation(self,headers,cookies,pre_res):
    #是否有关联
    headers_para,cookies_para = Base.params_find(headers,cookies)
    #有关联，执行前置用例，获取结果
    if len(headers_para):
        headers_data = pre_res["body"][headers_para[0]]
    #结果替换
        headers = Base.res_sub(headers,headers_data)
    if len(cookies_para):
        cookies_data = pre_res["body"][headers_para[0]]
    #结果替换
        cookies = Base.res_sub(headers,cookies_data)
    return headers,cookies

# TestExcel().test_run()
if __name__ == '__main__':
    #
    pytest.main(["-s","Test_excel_case.py"])
