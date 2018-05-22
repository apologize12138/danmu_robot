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
        self.danmu = ''
        self.nickname = ''

        #真实网址 获取弹幕---f12 网络 msg 消息头
        self.url_1 = 'https://api.live.bilibili.com/ajax/msg'
        #获取弹幕
        self.form1 = {'roomid': self.roomid,
                      'token':'',
                      'csrf_token':'b4bc76fe93d635b5a47f68989fb30faa'
        }
        self.url_2 = 'https://api.live.bilibili.com/msg/send'
        """
        self.cookie = {'Cookie': 'l=v; buvid3=75003816-F976-40CB-8658-4876FF056B798547infoc; finger=964b42c0;'
                                 ' LIVE_BUVID=58925189fc9d3285c4e9107977106eef; Hm_lvt_8a6e55dbd2870f0f5bc9194c'
                                 'ddf32a02=1516206018,1516206052,1516206078,1516252032; sid=ilsqem6n; fts=151619'
                                 '4841; DedeUserID=24195837; DedeUserID__ckMd5=d1c1cdef421589c7; SESSDATA=1b658c2'
                                 '1%2C1518786861%2Cf9f9e655; bili_jct=cdc7c79940b6eab70faf5f16b67e1f52; LIVE_BUVID'
                                 '__ckMd5=e23e03c1c88c3377; UM_distinctid=16104eb316d107-00069204dd6b4d8-173a7440-1'
                                 '00200-16104eb316e3f; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516252042; _dfcaptc'
                                 'ha=329cf06198f5a18766c986812664e2f1'}#你的cookies
        """
        self.cookie = {'Cookie': 'buvid3=1DD2673B-2239-4026-B917-F08D67DDB49012251infoc; LIVE_BUVID=58925189fc9d3285c4e9107977106eef; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1526999326,1526999597,1526999727,1527002582; sid=ilsqem6n; fts=1516194841; LIVE_BUVID__ckMd5=e23e03c1c88c3377; UM_distinctid=16104eb316d107-00069204dd6b4d8-173a7440-100200-16104eb316e3f; pgv_pvi=1838871552; rpdid=olpiixpmqpdosiwmpimiw; CURRENT_QUALITY=80; finger=964b42c0; DedeUserID=24195837; DedeUserID__ckMd5=d1c1cdef421589c7; SESSDATA=1b658c21%2C1529511381%2Cf89add44; bili_jct=b4bc76fe93d635b5a47f68989fb30faa; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1527002582; im_notify_type_24195837=0; _dfcaptcha=d2da6df93653ee20972092f35d647684'}
    def getDanMu(self):

        html_1 = requests.post(self.url_1, data = self.form1)
        hasnew = False
        while 1:
            if hasnew:
                break
            index = random.randint(9,9)
            ds = html_1.json()['data']['room'][index]['text']
            ns = html_1.json()['data']['room'][index]['nickname']
            #if ns == self.nickname and ds == self.danmu:
            #time.sleep(0.1)
            #continue
            self.nickname = ns
            self.danmu = ds
            hasnew = True
            print(str(index) + '::' + self.nickname + '----'+self.danmu)

    #发送弹幕
    def postDanMu(self):
        self.form2 = {'color':'16777215',
                      'csrf_token':'1527002580',
                      'fontsize':'25',
                      'mode':'1',
                      'msg':self.danmu,
                      'rnd':'1527002580',
                      'roomid': self.roomid}
        #print(self.form2)

        a = requests.post(self.url_2, data = self.form2, cookies = self.cookie)
        print(str(a) + '  '+'send---------'+self.danmu)

if __name__ == '__main__':
    flag = 1
    danmu = SendLiveRoll(273849)
    while 1:
        danmu.getDanMu()
        if flag < 3:
            danmu.postDanMu()
        flag += 1
        time.sleep(random.randint(3, 3))




