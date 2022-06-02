import requests
from utils.LogUtil import my_log
# def requests_get(url,headers):
#     r=requests.get(url,headers=headers)
#     code=r.status_code
#     try:
#         body=r.json()
#     except Exception as e:
#         body=r.text
#     res=dict()
#     res["code"]=code
#     res["body"]=body
#     return res
#
# def requests_post(url,json=None,headers=None):
#     r = requests_post(url,json=json,headers=headers)
#     code = r.status_code
#     try:
#         body = r.json()
#     except Exception as e:
#         body = r.text
#     res = dict()
#     res["code"] = code
#     res["body"] = body
#     return res

class Requests:
    def __init__(self):
        self.log = my_log("Requests")
    def requests_api(self,url,data = None,json = None,headers = None,method = "get",cookies=None):
        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(url,json = json,data = data,headers = headers, cookies=cookies)
        elif method == "post":
            self.log.debug("发送post请求")
            r = requests.post(url,json=json,data=data,headers=headers, cookies=cookies)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res["code"] = code
        res["body"] = body
        return res
    def get(self,url,**kwargs):
        return self.requests_api(url,method="get",**kwargs)

    def post(self, url, **kwargs):
        return self.requests_api(url, method="post", **kwargs)
