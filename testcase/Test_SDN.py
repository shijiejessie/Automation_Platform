from utils.RequestsUtil import Requests
from config.conf import ConfigYaml
import pytest
from utils.AssertUtil import AssertUtil
from common.Base import init_db
common_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

def test_login():

    conf_x = ConfigYaml()
    url_path = conf_x.get_conf_url()
    url = "http://"+ url_path + "/api/login"
    print(url)
    print(type(url))
    data = {"username":"longjq1","password":"SDNljq@1","verifyCode":"1111111"}
    request = Requests()
    r=request.post(url, json=data)
    print(r)
    c=r.get('body')
    d=c.get('data')
    authToken=d["authToken"]
    login_token1=authToken.split('.')[1]
    login_token2= authToken.split('.')[2]
    login_token = login_token1 + "."+login_token2
    return login_token
    code=r["code"]
    AssertUtil().assert_code(code,200)



def test_listvrr():
    conf_x = ConfigYaml()
    url_path = conf_x.get_conf_url()
    url = "http://" + url_path + "/api/deviceBase/list/vrr?currPage=1&pageSize=10"
    kkkk={"authToken" :common_token+"."+test_login()}
    print(kkkk)
    request=Requests()
    r = request.get(url,headers=kkkk)
    print(r)
    c = r.get('body')
    d = c.get('data')
    e = d.get('result')
    f = e[0]
    g = f.get('active')
    print(type(e))
    print(e)
    print(f)
    print(g)
    #建立连接
    conn = init_db("db_1")
    #查询结果
    res_db = conn.fetchone("SELECT cluster_id,active FROM device_base_vrr where region_name = '北京' ")
    print("数据库查询结果：%s",res_db)
    #结果验证
    assert g == res_db['active']




if __name__=="__main__":
    #test_login()
    #test_listvrr()
    pytest.main(["Test-SDN.py"])


