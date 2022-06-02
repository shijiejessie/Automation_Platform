from config import conf
import os
from utils.YamlUtil import YamlReader
import pytest
from config.conf import ConfigYaml
from utils.RequestsUtil import Requests
test_file = os.path.join(conf.get_data_path(),"testlogin.yml")

data_list = YamlReader(test_file).data_all()

@pytest.mark.parametrize("login",data_list)
def test_yaml(login):
    #初始化数据
    url = "http://" + ConfigYaml().get_conf_url() + login["url"]
    print("url %s"%url)
    data = login["data"]
    print("data %s"%data)
    #post请求
    request = Requests()
    res = request.post(url,json = data)
    print(res)
if __name__ == "__main__":
    pytest.main["-s","Test_login.py"]




#参数化执行测试用例