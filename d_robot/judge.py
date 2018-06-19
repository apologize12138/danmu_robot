#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import string

class Judge_Send():
    def __init__(self,base_data):
        with open('base_data.txt', 'w') as f1:
           for li in base_data:
               f1.writelines(li+'\n')
        with open('base_data.txt', 'r') as f2:
            list1 = f2.readlines()
            for i in range(0,len(list1)):
                list1[i] = list1[i].rstrip('\n')
            self.live_data = list1
            print(self.live_data)



    def need_send(self,text):
        for ls in self.live_data:
            if text.find(ls) != -1:
                text = ls
                return 1,text

        return 0,text