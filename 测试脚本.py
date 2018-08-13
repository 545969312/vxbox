"""
用于向指定用户发送消息
前提：
    1. 申请账号
        appID：
        wx31b231d076fa403c
        appsecret：
        16ff6c0fb48bc117db2b4f28e35b2453
    2. 知道用户的微信ID
        othEL0hlOrdBIRLLXuX0BA8frGZE

"""
import json
import requests

# 1. 伪造浏览器向 https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential... 发送GET请求，并获取token
r1 = requests.get(
    url="https://api.weixin.qq.com/cgi-bin/token",
    params={
        "grant_type": "client_credential",
        "appid": 'wx65d37317efb972e0',
        "secret": 'f59dc1e2f5e3641145a213027fb122cc',
    }
)

access_token = r1.json().get('access_token')

# 2. 给指定用户发送普通消息消息：access_token/
"""
wx_id = 'othEL0hlOrdBIRLLXuX0BA8frGZE'

body = {
    "touser": wx_id,
    "msgtype": "text",
    "text": {
        "content": '骑兵步兵'
    }
}

r2 = requests.post(
    url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
    params={
        'access_token': access_token
    },
    data=bytes(json.dumps(body,ensure_ascii=False),encoding='utf-8')
)

print(r2.text)
"""
# 3. 给指定用户发送模板消息：access_token/

wx_id = 'othEL0oARSWwZ0z7UvcMBzxuOLGQ'

body = {
    "touser": wx_id,
    "template_id": '2hG3SEQVaCGZ9NJPl5Mc1nWAiWN9_yB2qa44ciayYE4',
    "data": {
        "user": {
            "value": "孙奇兵",
            "color": "#173177"
        }
    }
}

r2 = requests.post(
    url="https://api.weixin.qq.com/cgi-bin/message/template/send",
    params={
        'access_token': access_token
    },
    data=json.dumps(body)
)

print(r2.text)











# response = requests.post(
#     url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
#     params={
#         'access_token': access_token
#     },
#     data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
# )
# # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
# result = response.json()
# print(result)