import wx
import time
import math
buttonID=300

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='简易计算器')
        self.resultStr = ''

        #菜单栏
        menuBar=wx.MenuBar()
        menu1=wx.Menu()
        menu1.Append(-1,'&New','create a new file')
        menu1.Append(wx.NewId(),'&Exit','this is exit')
        menu2=wx.Menu()
        menuBar.Append(menu1,'File(&F)')
        menuBar.Append(menu2,'&Help(&H)')
        self.SetMenuBar(menuBar)

        #状态栏
        statusBar=self.CreateStatusBar(2)
        self.SetStatusWidths([-1,-2])
        self.SetStatusText('时间：',0)
        self.timer=wx.PyTimer(self.Notify)
        self.timer.Start(1000,wx.TIMER_CONTINUOUS) #连续运行
        self.Notify()
        self.SetStatusText('',1)

        #工具栏
        toolBar=self.CreateToolBar()
        toolBar.SetBackgroundColour('white')
        bmp = wx.Image('01.png', wx.BITMAP_TYPE_PNG)
        bmp = wx.Bitmap(bmp.Rescale(20, 20))
        toolBar.AddSimpleTool(wx.NewId(), bmp, "new", 'long help for New')
        toolBar.Realize()  # 准备显示工具栏

        panel = wx.Panel(self, size=(-1,-1))

        vbox=wx.BoxSizer(wx.VERTICAL)
        self.ct=wx.TextCtrl(panel,-1,size=(-1,30))
        vbox.Add(self.ct,0,wx.EXPAND|wx.ALL,20)

        g=wx.GridSizer(6,5,5,5)
        list='7 8 9 DEL AC 4 5 6 * / 1 2 3 + - 0 % PI e sqrt ^ sin cos tan log ln ( ) . ='.split()
        global buttonID
        buttonlist=[]
        for i,s in enumerate(list):
            g.Add(wx.Button(panel,id=buttonID+i,label='{}'.format(s),size=(60,70)), 0, wx.EXPAND | wx.ALL,2)
            # buttonlist.append(wx.Button(panel,id=buttonID+i,label='{}'.format(s),size=(60,50)))
            self.Bind(wx.EVT_BUTTON,self.buttonOnClick,id=buttonID+i)
        # g.AddMany(buttonlist)


        vbox.Add(g, 0, wx.EXPAND|wx.LEFT|wx.RIGHT,30)
        panel.SetSizer(vbox)

    def buttonOnClick(self,event):
        # e=event.GetEventObject()
        # str=''
        # str=str+e.GetLabel()
        # print(str)

        print(event.GetId())
        mathFunc = ['sqrt', 'sin', 'cos', 'tan']
        result = 'Error'
        if event.GetEventObject().GetLabel() == '=':
            print("=")
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
            self.ct.SetValue(result)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'AC':
            '''click button "AC" to clear screen'''
            self.ct.SetValue('')
            self.resultStr = ''
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'DEL':
            '''click button "DEL" to Undo'''
            self.resultStr = self.resultStr[:-1]
            self.ct.SetValue(self.resultStr)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'e':
            '''e=math.e'''
            self.resultStr += str(math.e)
            self.ct.SetValue(self.resultStr)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'PI':
            '''pi=3.1416'''
            self.resultStr += str(math.pi)
            self.ct.SetValue(self.resultStr)
            event.Skip()
        else:
            self.resultStr += event.GetEventObject().GetLabel()
            self.ct.SetValue(self.resultStr)
            event.Skip()







    def Notify(self):
        t=time.localtime(time.time())
        st=time.strftime('%Y-%m-%d %H:%M:%S',t)
        self.SetStatusText(st,1)

if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,-1)
    frame.Show()
    app.MainLoop()
