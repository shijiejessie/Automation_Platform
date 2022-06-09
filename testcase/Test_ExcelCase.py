import json
import ast
from config.conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Requests
import pytest
from common import Base
from utils.AssertUtil import AssertUtil
from common.Base import init_db
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
        print("前置用例执行： %s"%res)
        return res

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
        response_assert = case[data_key.response_assert]
        if pre_exec:
            pre_case = data_init.get_case_pre(pre_exec)
            # print("前置条件为： %s"%pre_case)
            pre_res = self.run_pre(pre_case)
            pre_res = pre_res["body"]["data"]["authToken"]
            headers = self.get_correlation(headers,pre_res)
        res = self.run_api(url , method ,params ,headers)
        print("测试用例执行 %s"% res)
        # #状态码验证
        assert_util = AssertUtil()
        assert_util.assert_code(int(res["code"]),int(status_code))
        # #验证返回内容,包含
        assert_util.assert_in_body(str(res["body"]),expect_result)
        #数据库校验，初始化数据库，查询SQL，结果验证
        sql = init_db("db_1")
        db_res = sql.fetchone(db_assert)
        log.debug("数据库查询结果:{}".format(str(db_res)))
        #获取数据库的Key,根据key获取数据库结果、接口结果，再验证
        verify_list = list(dict(db_res).keys())
        result = res["body"]["data"]["result"][0]
        response_assert2 = ast.literal_eval(response_assert)
        list1 = []
        list2 = []
        for line in verify_list:
            res_db_line = dict(db_res)[line]
            list1.append(res_db_line)
        for line in response_assert2:
            res_line = dict(result)[line]
            list2.append(res_line)
        diff = list(set(list1).difference(set(list2)))
        diff.extend(list(set(list2).difference(set(list1))))
        if diff == []:
            print("通过：数据库字段值与接口返回值一致")
        else:
            print(False)
    def get_correlation(self,headers,pre_res):
        headers_params = Base.params_find(headers)
        if len(headers_params):
            headers_data = pre_res
            headers = Base.res_sub(headers,headers_data)
        return headers

if __name__ == "__main__":
    pytest.main(["-s","Test_ExcelCase.py"])
