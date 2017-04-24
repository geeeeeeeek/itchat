#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-04-24 21:48:35
# @Last Modified by:   Marte
# @Last Modified time: 2017-04-24 22:23:51
# import itchat,time, re
# from itchat.content import *
# import urllib2, urllib 
# import json

# @itchat.msg_register([TEXT])
# def text_reply(msg):
#     info = msg['Text'].encode('UTF-8')
#     url = 'http://www.tuling123.com/openapi/api'
#     data = {}
#     
#     
#     
# import requests
# from wxpy import *
# import json


#图灵机器人
# def talks_robot(info = '你叫什么名字'):
#     api_url = 'http://www.tuling123.com/openapi/api'
#     apikey = 'cdd4f8362ad24ab5aae007d97d6fb35f'
#     data = {'key': apikey, 'info': info}
#     req = requests.post(api_url, data=data).text
#     replys = json.loads(req)['text']
#     return replys

# #微信自动回复
# robot = Robot()
# # 回复来自其他好友、群聊和公众号的消息
# @robot.register()
# def reply_my_friend(msg):
#     message = '{}'.format(msg.text)
#     replys = talks_robot(info=message)
#     return replys

# # 开始监听和自动处理消息
# robot.start()
# 
# 
import time
from wxbot import *

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

    def schedule(self):
        self.send_msg(u'tb', u'schedule')
        time.sleep(1)

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.run()

if __name__ == '__main__':
    main()