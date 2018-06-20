#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from tkinter import *
import time
import os
import _thread,threading


def main():
    def run_send(threadname = ''):
        os.system('python Send.py')
    def run_show_live_data(threadname = ''):
        os.system('python show_live_data.py')
    def btn_run_send():
        try:
            _thread.start_new_thread(run_show_live_data(),('thread2'))
        except:
            print('ERROR 线程启动失败')
    def btn_stop_send():
        a =1



    '''
    num = 0
    root = tkinter.Tk(className='请输入直播间roomid')  # 弹出框框名
    root.geometry('270x60')  # 设置弹出框的大小 w x h

    var = tkinter.StringVar()  # 这即是输入框中的内容
    var.set(r_id)  # 通过var.get()/var.set() 来 获取/设置var的值
    entry1 = tkinter.Entry(root, textvariable=var)  # 设置"文本变量"为var
    entry1.pack()  # 将entry"打上去"
    btn1 = tkinter.Button(root, text='Input', command=inputint)  # 按下此按钮(Input), 触发inputint函数
    btn2 = tkinter.Button(root, text='Clear', command=inputclear)  # 按下此按钮(Clear), 触发inputclear函数

    # 按钮定位
    btn2.pack(side='right')
    btn1.pack(side='right')

    # 上述完成之后, 开始真正弹出弹出框
    root.mainloop()
    '''

    # 创建窗口
    t = Tk()
    t.title('ROBOT--WB')
    t.geometry('400x300')

    btn1 = Button(t, text='运行ROBOT', command=btn_run_send)  # 按下此按钮(Input), 触发inputint函数
    btn1.pack(side='right')
    btn2 = Button(t, text='停止ROBOT', command=btn_stop_send)  # 按下此按钮(Input), 触发inputint函数
    btn2.pack(side='right')

    # 主事件循环
    t.mainloop()


if __name__ == '__main__':

    main()
