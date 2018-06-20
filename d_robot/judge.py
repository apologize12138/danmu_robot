#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
class Judge_Send():
    def __init__(self,base_data):
        with open('base_data.txt', 'w') as f1:
           for li in base_data:
               f1.write(li+'\n')
        with open('base_data.txt', 'r') as f2:
            list1 = f2.readlines()
            for i in range(0,len(list1)):
                list1[i] = list1[i].rstrip('\n')
            self.live_data = list1
            #print(self.live_data)



    def need_send(self,text):
        if text.find('机器人') != -1:
            print('被发现了，溜了溜了')
            sys.exit(0)
        for ls in self.live_data:
            if text.find(ls) != -1:
                if type(ls) == list:
                    print(ls)
                    sys.exit(0)
                text = ls
                return 1,text

        return 0,text

    def update_data(self,list1):
        rt = []
        with open('live_data.txt', 'a+') as f1:
            for li in list1:
               flag_1 = 0
               for si in self.live_data:
                   if si.find(li) != -1:
                       flag_1 = 1
                       break
               if flag_1 == 0:
                   self.live_data.append(li)
                   rt.append(li)
                   f1.write(li + '\n')

        print('add word')
        print(rt)
