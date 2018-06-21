#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from tkinter import *
import time
import os
import _thread,threading
import inspect
import ctypes
import subprocess

_pid1 = 123
_pid2 = 456

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def main():
    def run_send(threadname = ''):
        global _pid1
        _pid1 = subprocess.Popen(r'python Send.py').pid

    def run_show_live_data(threadname = ''):
        global _pid2
        _pid2 = subprocess.Popen(r'python show_live_data.py').pid

    def run_show_base_data(threadname = ''):
        global _pid2
        _pid2 = subprocess.Popen(r'python show_base_data.py').pid

    def run_show_my_send_data(threadname = ''):
        global _pid2
        _pid2 = subprocess.Popen(r'python show_my_send_data.py').pid

    def btn_stop_send():
        os.system('taskkill /f /pid %s' %_pid1)


    # 创建窗口
    t = Tk()
    t.title('ROBOT--WB')
    t.resizable(False,False)
     # t.update()  # update window ,must do
    curWidth = 406
    curHeight = 250
    scnWidth, scnHeight = t.maxsize()  # get screen width and height
    #print(curWidth,curHeight,scnWidth,scnHeight)
    # now generate configuration information
    tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                              (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
    t.geometry(tmpcnf)

    w1 = Frame(height=200, width=406)
    w2 = Frame(height=50, width= 406)
    w1.grid_propagate(0)
    w2.grid_propagate(0)
    w1.grid(row=0, column=0, padx=0, pady=5)
    w2.grid(row=1, column=0, padx=0, pady=0)
    t1 = w1
    t2 = w2
    t1.grid()
    t2.grid()
    photo1 = PhotoImage(file = "robot.gif")
    theLabel = Label(t1,
                        text = "",
                        # 内容
                        justify = LEFT,
                        # 对齐方式
                        image = photo1,
                        # 加入图片
                        compound = CENTER,
                        # 关键:设置为背景图片
                        font = ("华文行楷", 20),
                        # 字体和字号
                        fg = "white")  # 前景色
    theLabel.pack()

    btn1 = Button(t2, text='运行ROBOT', command=run_send)  # 按下此按钮(Input), 触发inputint函数
    btn1.pack(side='left')
    btn2 = Button(t2, text='停止ROBOT', command=btn_stop_send)  # 按下此按钮(Input), 触发inputint函数
    btn2.pack(side='left')
    btn3 = Button(t2, text='显示基本词库', command=run_show_base_data)  # 按下此按钮(Input), 触发inputint函数
    btn3.pack(side='left')
    btn4 = Button(t2, text='显示最新词库', command=run_show_live_data)  # 按下此按钮(Input), 触发inputint函数
    btn4.pack(side='left')
    btn5 = Button(t2, text='显示发送纪录', command=run_show_my_send_data)  # 按下此按钮(Input), 触发inputint函数
    btn5.pack(side='left')

    # 主事件循环
    t.mainloop()


if __name__ == '__main__':

    main()
