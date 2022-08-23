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


        self.buttonOK=wx.Button(self.panel,-1,'OK',(20,20),(60,30))
        self.Bind(wx.EVT_BUTTON,self.Onclick,self.buttonOK)
        self.buttonCancel=wx.Button(self.panel,-1,'Cancel',(20,80),(60,30))
        self.Bind(wx.EVT_BUTTON,self.Onclick,self.buttonCancel)


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