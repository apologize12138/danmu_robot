#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import queue

msg_q_l = 10

class Study_Robot():        #别的小朋友都在学习，你不学习的吗？
    def __init__(self):
        self.msg_q = queue.deque(maxlen=msg_q_l)

    def get(self,text):
        self.msg_q.append(text)
        print(self.msg_q)
