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
    if re_res:
        return re.sub(pattern_data,replace,data)
    return re_res
#验证请求中是否${}$需要结果关联
def params_find(headers,cookies):
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return headers,cookies

if __name__ == "__main__":
    #init_db("db_1")
    print(res_find('{"authToke":"${token}$"}'))
    print(res_sub('{"authToke":"${token}$"}',"123"))
