# coding=gb2312
from config.conf import ConfigYaml
from utils.MysqlUtil import Mysql
import re
#定义init_db
p_data = '\${(.*)}\$'
def init_db(db_alias):
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
#初始化数据信息，通过配置
    conn = Mysql( host ,  user , password, db_name, charset, port )
    print(conn)
    return conn
#查询
def res_find(data,pattern_data=p_data):
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res
#替换
def res_sub(data,replace,pattern_data=p_data):
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    #拿repalce替换data,pattern_data为正则表达，可不传
    if re_res:
        return re.sub(pattern_data,replace,data)
    return re_res

def params_find(headers):
    if "${" in headers:
        headers = res_find(headers)
    return headers

# def json_parse():
#     if len(str(params).strip()) == 0:
#         headers = eval(headers)
#     if len(str(headers).strip()) == 0:
#         params = eval(params)

if __name__ == "__main__":
    init_db("db_1")
    #print(res_find('{"authToke":"${token}$"}'))
    #print("lalala"+res_sub('{"authToke":"${token}$"}',"123"))
