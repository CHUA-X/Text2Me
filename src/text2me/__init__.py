#! /usr/bin/python3
# text2me ——通过Twilio发消息给自己手机
# 用法：准备一个txt文件，按照以下格式布局：
# 账户SID
# AUTH认证标识
# 发送者手机号（必须加国家号）
# 接收者手机号（必须加国家号）
# import text2me;text2me.send('消息', '文件路径')

from twilio.rest import Client


def send(msg, config_file):
    with open(config_file) as f:
        account_sid, auth_token, from_phone, to_phone = f.readlines()
    Client(account_sid, auth_token).messages.create(body=msg, from_=from_phone, to=to_phone)
