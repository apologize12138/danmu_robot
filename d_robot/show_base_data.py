#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
class sbd():
    def __init__(self):
        self.base_data = []
        with open('base_data.txt', 'r') as f2:
            list1 = f2.readlines()
            for i in range(0,len(list1)):
                list1[i] = list1[i].rstrip('\n')
            self.base_data = list1

if __name__ == '__main__':
    show_base_data = sbd()
    print('\n\n')
    print(show_base_data.base_data)
    print('\n\n')