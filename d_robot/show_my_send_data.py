#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
class sbd():
    def __init__(self):
        self.my_send_data = []
        with open('my_send_data.txt', 'r') as f2:
            list1 = f2.readlines()
            for i in range(0,len(list1)):
                list1[i] = list1[i].rstrip('\n')
            self.my_send_data = list1

if __name__ == '__main__':
    show_my_send_data = sbd()
    print(show_my_send_data.my_send_data)