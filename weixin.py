#!/usr/bin/python3
# coding=utf-8


import itchat,code,unicodedata
import requests,re
from urllib.parse import quote,unquote

# Your wechat account may be LIMITED to log in WEB wechat, error info:
# <error><ret>1203</ret><message>为了你的帐号安全，此微信号已不允许登录网页微信。你可以使用Windows微信或Mac微信在电脑端登录。Windows微信下载地址：https://pc.weixin.qq.com  Mac微信下载地址：https://mac.weixin.qq.com</message></error>
# Start auto replying.

# 参考文章： https://segmentfault.com/a/1190000009420701

def get_reply(data):
    ini = "{'sessionId':'09e2aca4d0a541f88eecc77c03a8b393','robotId':'webbot','userId':'462d49d3742745bb98f7538c42f9f874','body':{'content':'" + data + "'},'type':'txt'}&ts=1529917589648"
    url = "http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=" + quote(ini)
    cookie = {"cnonce": "808116", "sig": "0c3021aa5552fe597bb55448b40ad2a90d2dead5",
              "XISESSIONID": "hlbnd1oiwar01dfje825gavcn", "nonce": "273765", "hibext_instdsigdip2": "1"}
    r = requests.get(url, cookies=cookie)
    print(r.text)
    pattern = re.compile(r'\"fontColor\":0,\"content\":\"(.*?)\"')
    result = pattern.findall(r.text)
    print(result[1])
    return result[1]

def webot_chat(data):
    # curl http://11.11.152.240:8898/ -d '{"question": "你们有什么产品", "uid": "1234567"}'
    r = requests.post('http://11.11.152.240:8898/', json={"question": data, "uid": "1234567"})
    ret = r.json()
    answer = ret.get('answer', '抱歉，不知道呢；')
    return answer

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    """接收消息后回复消息；"""
    print(msg['Text'])
    print(msg['FromUserName'])
    datas=get_reply(msg['Text'])[:-4]
    # datas=webot_chat(msg['Text'])
    print(datas)
    itchat.send(datas, toUserName=msg['FromUserName'])

def get_friends():
    friends = itchat.get_friends(update=True)  # 获取微信好友列表，如果设置update=True将从服务器刷新列表
    for i in friends:
        print(i)


def main():
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()


if __name__ == '__main__':
    main()