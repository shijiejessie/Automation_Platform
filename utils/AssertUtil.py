import json

from utils.LogUtil import my_log

class AssertUtil:
    def __init__(self):
        self.log = my_log("AssertUtil")

    def assert_code(self,code,expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code is erro, code is %s ,expected_code is %s"%(code,expected_code))
            raise

    def assert_body(self,body,expected_body):
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("body is erro ,body is %s , expected_body is %s"%(body,expected_body))
            raise
    def assert_in_body(self,body,expected_body):
        try:
            body == json.dumps(body)
            assert expected_body in body
            return True
        except:
            self.log.error("不包含或者Body错误, body is %s ,expected_body is %s"%(body,expected_body))
