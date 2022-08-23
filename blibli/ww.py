#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################################
# Write   : 2019-3-29
# Author  : 樊晓鑫
# File    : wxPython初级教程之第10课 : 优化版简易计算器
# Content : 面板(panel)的设计
#########################################################################################

import wx
import math

ID_CALC = 300


class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)

        ## 定义为全局变量
        global ID_CALC

        ## 定义存储在文本中的变量
        self.resultStr = ''

        ## 放置可控文本，用于保持计算结果
        self.calcResult = wx.TextCtrl(self, -1, '', pos=(20, 10), size=(250, 50), style=wx.TE_MULTILINE | wx.TE_RICH2)
        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.BOLD, underline=False)
        self.calcResult.SetFont(font)

        ## 放置按钮
        botton_list = ['7', '8', '9', 'DEL', 'AC', '4', '5', '6', '*', '/', '1', '2', '3', '+', \
                       '-', '0', '%', 'PI', 'e', 'sqrt', '^', 'sin', 'cos', 'tan', 'log', 'ln', \
                       '(', ')', '.', '=']
        for i, button in enumerate(botton_list):
            wx.Button(self, ID_CALC, label="{}".format(button), pos=(20 + 50 * (i % 5), 70 + 50 * (i / 5)),
                      size=(50, 40))
            ## 绑定按钮功能
            self.Bind(wx.EVT_BUTTON, self.OnCalcClick, id=ID_CALC)
            ## ID自动加1，保持唯一性
            ID_CALC = ID_CALC + 1

    ## 显示文本控件中的内容
    def setText(self, value):
        '''set the value of TextCtrl'''
        self.calcResult.SetValue(value)

    ## 每个按钮的具体行为
    def OnCalcClick(self, event):
        print
        event.GetId()
        mathFunc = ['sqrt', 'sin', 'cos', 'tan']
        result = 'Error'
        if event.GetEventObject().GetLabel() == '=':
            print
            "="
            for func in mathFunc:
                if func in self.resultStr:
                    try:
                        result = str(eval('math.' + self.resultStr))
                        break
                    except:
                        pass
            if '^' in self.resultStr:
                try:
                    temp = self.resultStr.split('^')
                    result = str(eval('pow(' + temp[0] + ',' + temp[1] + ')'))
                except:
                    pass
            elif 'ln' in self.resultStr:
                try:
                    result = str(eval('math.log' + self.resultStr[2:]))
                except:
                    pass
            elif 'log' in self.resultStr:
                try:
                    result = str(eval('math.log' + self.resultStr[3:] + '/math.log(10)'))
                except:
                    pass
            else:
                try:
                    result = str(eval(self.resultStr))
                except:
                    pass

            self.resultStr = result
            self.setText(result)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'AC':
            '''click button "AC" to clear screen'''
            self.calcResult.SetValue('')
            self.resultStr = ''
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'DEL':
            '''click button "DEL" to Undo'''
            self.resultStr = self.resultStr[:-1]
            self.setText(self.resultStr)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'e':
            '''e=math.e'''
            self.resultStr += str(math.e)
            self.setText(self.resultStr)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'PI':
            '''pi=3.1416'''
            self.resultStr += str(math.pi)
            self.setText(self.resultStr)
            event.Skip()
        else:
            self.resultStr += event.GetEventObject().GetLabel()
            self.setText(self.resultStr)
            event.Skip()