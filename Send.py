#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#导入模块
import requests #1.
import time
import random

class SendLiveRoll():
    #初始化函数
    def __init__(self,roomid): #roomid 房间号

        #直播间房间号
        self.roomid = roomid

        #真实网址 获取弹幕---f12 网络 msg 消息头
        self.url_1 = 'https://api.live.bilibili.com/ajax/msg'
        #获取弹幕
        self.form1 = {'roomid': self.roomid,
                      'token':'',
                      'csrf_token':'070ac5b8137744aab1d557d86bdd94b0'
        }
        self.url_2 = 'https://api.live.bilibili.com/msg/send'
        self.cookie = {'Cookie': 'l=v; buvid3=75003816-F976-40CB-8658-4876FF056B798547infoc; finger=964b42c0; LIVE_BUVID=58925189fc9d3285c4e9107977106eef; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516206018,1516206052,1516206078,1516252032; sid=ilsqem6n; fts=1516194841; DedeUserID=24195837; DedeUserID__ckMd5=d1c1cdef421589c7; SESSDATA=1b658c21%2C1518786861%2Cf9f9e655; bili_jct=cdc7c79940b6eab70faf5f16b67e1f52; LIVE_BUVID__ckMd5=e23e03c1c88c3377; UM_distinctid=16104eb316d107-00069204dd6b4d8-173a7440-100200-16104eb316e3f; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516252042; _dfcaptcha=329cf06198f5a18766c986812664e2f1'}#你的cookies

    def getDanMu(self):

        html_1 = requests.post(self.url_1, data = self.form1)

        self.danmu = html_1.json()['data']['room'][random.randint(7,9)]['text']
        print(self.danmu)

    #发送弹幕
    def postDanMu(self):
        self.form2 = {'color':'16777215',
                      'fontsize':'25',
                      'mode':'1',
                      'msg':self.danmu,
                      'rnd':'15967170365',
                      'roomid': self.roomid}

        requests.post(self.url_2, data = self.form2, cookies = self.cookie)

if __name__ == '__main__':
    while 1:

        danmu = SendLiveRoll(273849)
        danmu.getDanMu()
        danmu.postDanMu()
        time.sleep(random.randint(1, 1))




