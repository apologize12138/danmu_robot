# 导入模块
import requests  # 1. 网络请求  2.pip install requests
import time  # 用于时间控制
import random  # 随机模块 产生随机数

class SendLiveRoll():

    # 会自己先一步其他函数执行, 初始化函数
    def __init__(self, roomid):  # roomid 直播的房间号 273849

        # 初始化直播的房间号
        self.roomid = roomid

        # 获取弹幕的真实网址
        self.url_1 = 'https://api.live.bilibili.com/ajax/msg'
        self.form1 = {'roomid': self.roomid,
                      'token': ' ',
                      'csrf_token': '070ac5b8137744aab1d557d86bdd94b0'
                      }
        # 获取发送弹幕幕的真实网址
        self.url_2 = 'https://api.live.bilibili.com/msg/send'
        # 获取cookie
        self.cookie = {'Cookie': 'buvid3=1DD2673B-2239-4026-B917-F08D67DDB49012251infoc; LIVE_BUVID=58925189fc9d3285c4e9107977106eef; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1526967526,1526988448,1526988708,1526989301; sid=ilsqem6n; fts=1516194841; LIVE_BUVID__ckMd5=e23e03c1c88c3377; UM_distinctid=16104eb316d107-00069204dd6b4d8-173a7440-100200-16104eb316e3f; pgv_pvi=1838871552; rpdid=olpiixpmqpdosiwmpimiw; CURRENT_QUALITY=80; finger=964b42c0; DedeUserID=24195837; DedeUserID__ckMd5=d1c1cdef421589c7; SESSDATA=1b658c21%2C1529511381%2Cf89add44; bili_jct=b4bc76fe93d635b5a47f68989fb30faa; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1526989301; im_notify_type_24195837=0; _dfcaptcha=03776b7919c0e878d59bf07c55a30407'}   # 你的Cookies
    # 获取弹幕的函数
    def getDanMu(self):

        # 获取弹幕
        html_1 = requests.post(self.url_1, data=self.form1)

        # 提取弹幕
        self.danmu = html_1.json()['data']['room'][random.randint(0, 3)]['text']
        print(self.danmu)

        # 发送弹幕的函数
    def sendDanMu(self):
        t = time.time()
        self.form2 = {'color': '16777215',
                      'fontsize': '25',
                      'mode': '1',
                      'msg': self.danmu,
                      'rnd': int(t),
                      'roomid': self.roomid}
        requests.post(self.url_2, data=self.form2, cookies=self.cookie)




if __name__ == '__main__':

    flag = 0;
    while True:
        time.sleep(random.randint(2, 6))
        danmu = SendLiveRoll(273849)
        danmu.getDanMu()
        if flag == 0:
            danmu.sendDanMu()
        flag += 1