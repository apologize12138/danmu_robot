#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import queue
import sys

msg_q_l = 10
yuzhi = 2

class Study_Robot():        #别的小朋友都在学习，你不学习的吗？
    def __init__(self):
        self.msg_q = queue.deque(maxlen=msg_q_l)

    def add_text(self,text):
        word = []
        weight = []
        len2 = len(text)
        ls_t = []
        for i in range(0, len2 - 1):
            ls_ts = []
            for j in range(0, len2 - i - 1):
                sub_s = ''
                for c in range(i, len2 - j):
                    sub_s = sub_s + text[c]

                ls_ts.append(sub_s)
            ls_t.append(ls_ts)
        #print(ls_t)

        for s in self.msg_q:#产生词汇池
            for s1 in ls_t:
                for s2 in s1:
                    if s.find(s2) != -1:
                        #print(s2)
                        flag_ws = 0
                        for ws_i in range(0,len(word)):
                            if s2==word[ws_i]:
                                weight[ws_i]+=1
                                flag_ws = 1
                                break
                        if flag_ws == 0:
                            word.append(s2)
                            weight.append(1)
                    break
        rt = []
        max = 0
        for ws_i in range(0,len(word)):
            weight[ws_i] = weight[ws_i] * (len(word[ws_i]) - 1)
            if max < weight[ws_i]:
                max = weight[ws_i]
        for ws_i in range(0,len(word)):
            if weight[ws_i] >= max and weight[ws_i] >= yuzhi:
                rt.append(word[ws_i])
        self.msg_q.append(text)
        #print(self.msg_q)
        if len(rt) != 0:
            print('add words max = '+ str(max))
            print(rt)
        return rt

    def is_number(self,str_text):
        number = '0123456789'
        for i in range(0,len(str_text)):
            if number.find(str_text[i]) == -1:
                return False
        return True