#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#导入模块
import requests #1.
import time
import random
import judge
import study

#程序运行判断。。。全局
Start = 0
need_send = 1
need_study = 0
Robot_Time = 1#range in  (1,6)自适应
my_ns = "烟雨s浮尘"
base_data = {'23333','6666','flag','前方高能','高能','233', '666',  '康纳', '卡拉',  '马库斯', '帅','哈哈','晚安'
            ,'nb','牛逼','皮一下','厉害','握把','嘤嘤嘤','???','溜了','凉凉' ,'穷','细','吃鸡','五开','神仙','空投'
            ,'可爱','刺激','舒服了','777','88'
             }


#参数
r_id = 3495920

class SendLiveRoll():
    #初始化函数
    def __init__(self,roomid): #roomid 房间号

        #直播间房间号
        self.roomid = roomid
        self.text = ''#弹幕内容
        self.nickname = ''#发送者
        self.jd = judge.Judge_Send(base_data)#judge实例
        self.sd = study.Study_Robot()#study实例

        #真实网址 获取弹幕---f12 网络 msg 消息头
        self.url_1 = 'https://api.live.bilibili.com/ajax/msg'
        #获取弹幕
        self.form1 = {'roomid': self.roomid,
                      'token':'',
                      'csrf_token':'b4bc76fe93d635b5a47f68989fb30faa'
        }
        self.url_2 = 'https://api.live.bilibili.com/msg/send'
        self.cookie = {'Cookie': 'l=v; finger=edc6ecda; buvid3=D8C24A24-E921-467E-A09B-96AB785CCAAD103050infoc;'
                                 'LIVE_BUVID=AUTO7915269904519694; sid=anepyb3s; DedeUserID=24195837;'
                                 ' DedeUserID__ckMd5=d1c1cdef421589c7; SESSDATA=1b658c21%2C1529582489%2C570377d3;'
                                 ' bili_jct=5fa697f73143af565b13404751284e84; _dfcaptcha=cf805f27c675bc9decfa47f93b62ba18;'
                                 ' Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1526990469,1527085312,1527085722,1527085820;'
                                 ' Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1527085820'}##############我的cookies

    def getDanMu(self):

        html_1 = requests.post(self.url_1, data = self.form1)
        #---------------------
        index = 9
        global Start
        global need_send
        global need_study
        need_send = 1
        ds = html_1.json()['data']['room'][index]['text']
        ns = html_1.json()['data']['room'][index]['nickname']
        if Start == 0:
             Start = 1
        else:
            #if ns == my_ns or (ns == self.nickname and ds == self.text):
            if (ns == self.nickname and ds == self.text):
                need_send = 0

        self.nickname = ns
        self.text = ds
        if need_send == 1:
            need_study = 1
            print("new msg  "+ str(index) + '::' + self.nickname + '----' + self.text)

    #发送弹幕
    def postDanMu(self):
        self.form2 = {'color':'16777215',
                      'fontsize':'25',
                      'mode':'1',
                      'msg':self.text,
                      'rnd':'1527085818',
                      'roomid': self.roomid,
                      'csrf_token':'5fa697f73143af565b13404751284e84'}
        #print(self.form2)

        a = requests.post(self.url_2, data = self.form2, cookies = self.cookie)
        print('send---------'+self.text)

    def judge(self):
        # --------------------
        global need_send
        rt = self.jd.need_send(self.text)  # 判断是否需要发送
        need_send = rt[0]
        self.text = rt[1]

    def study(self):
        print('have studied')

    def run_send(self):
        #--------------------
        global need_send
        if need_send == 1:
            self.postDanMu()

if __name__ == '__main__':
    flag = 1
    danmu = SendLiveRoll(r_id)
    while 1:
        danmu.getDanMu()
        if danmu.nickname != my_ns:
            need_send = 0
            danmu.judge()
            if need_study == 1:
                danmu.study()
                need_study = 0
            if need_send == 1:
                danmu.run_send()
        time.sleep(Robot_Time)



