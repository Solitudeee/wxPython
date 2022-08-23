import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        self.count=0
        self.gauge=wx.Gauge(self.panel,-1,100,pos=(50,80),size=(250,25))
        # self.gauge.SetBezelFace(3)
        # self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE,self.OnIdle)

    def OnIdle(self,event):
        self.count=self.count+1
        if self.count>=100:
            self.count=0
        self.gauge.SetValue(self.count)


if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()