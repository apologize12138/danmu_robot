#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Judge_Send():
    def __init__(self,base_data):
        self.live_data  = base_data

    def need_send(self,text):
        for ls in self.live_data:
            if text.find(ls) != -1:
                text = ls
                return 1,text

        return 0,''