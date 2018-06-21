#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
class sbd():
    def __init__(self):
        self.live_data = []
        with open('live_data.txt', 'r') as f2:
            list1 = f2.readlines()
            for i in range(0,len(list1)):
                list1[i] = list1[i].rstrip('\n')
            self.live_data = list1

if __name__ == '__main__':
    show_live_data = sbd()
    print('\n\n')
    print(show_live_data.live_data)
    print('\n\n')