import wx
import time
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,size=(500,500))
        self.panel=wx.Panel(self)
        #设置两个状态栏
        sb=self.CreateStatusBar(2)
        #宽度比是1:2
        self.SetStatusWidths([-1,-2])
        #0代表设置第一个状态栏文字
        self.SetStatusText('Ready',0)
        #timer
        self.timer=wx.PyTimer(self.Notify)
        self.timer.Start(1000,True)  #只调用一次
        # self.timer.Start(1000,False)  #重复调用直到计时器停止
        # self.timer.Start(1000,wx.TIMER_CONTINUOUS) #连续运行
        self.Notify()




        #设置菜单栏
        menuBar = wx.MenuBar()  # 创建菜单栏
        menu1 = wx.Menu()
        menu1.Append(wx.NewId(), '&new', 'creat a new file')
        item=menu1.Append(wx.NewId(),'&Exit','退出')
            #绑定事件
        self.Bind(wx.EVT_MENU,self.onExit,item)
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        # 6 创建菜单的项目
        menu2.Append(wx.NewId(), '&Copy', 'Copy in status bar')
        menu2.Append(wx.NewId(), 'C&ut', '')
        menu2.Append(wx.NewId(), 'Paste', "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), '&Options...', 'Display Options')
        menuBar.Append(menu2, '&Edit')
        self.SetMenuBar(menuBar)
        #登录
        self.name=wx.StaticText(self.panel,-1,'姓名:',pos=(50,120))
        self.pwd=wx.StaticText(self.panel,-1,'密码:',pos=(50,150))
        self.username=wx.TextCtrl(self.panel,-1,pos=(120,120))
        self.password=wx.TextCtrl(self.panel,-1,pos=(120,150))
        self.buttonSubmit = wx.Button(self.panel, -1, '提交', pos=(60, 200))
        self.buttonCancel = wx.Button(self.panel, -1, '清空', pos=(200, 200))
        self.Bind(wx.EVT_BUTTON,self.submit,self.buttonSubmit)
        self.Bind(wx.EVT_BUTTON,self.cancel,self.buttonCancel)

    def submit(self,event):
        name=self.username.GetValue()
        pd=self.password.GetValue()
        str="姓名:"+name+'\n密码:'+pd
        dlg1 = wx.MessageDialog(self.panel, str, 'MessageDialog',
                                wx.YES_NO | wx.ICON_QUESTION)
        result = dlg1.ShowModal()
        dlg1.Destroy()

    def onExit(self,event):
        self.Destroy()

    def cancel(self,event):
        self.username.Clear()
        self.password.Clear()

    def Onclick(self,event):
        if event.GetEventObject()==self.buttonOK:
            print("{}".format(event.GetEventObject().GetLabel()))

        if event.GetEventObject()==self.buttonCancel:
            print('cancel')

    def Notify(self):
        t=time.localtime(time.time())
        st=time.strftime('%Y-%m-%d %H:%M:%S',t)
        self.SetStatusText(st,1)


class app(wx.App):
    def OnInit(self):
        f=MyFrame(None,-1)
        f.Show(True)
        return True
if __name__=='__main__':
    a=app()
    a.MainLoop()