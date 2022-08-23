import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'MyFrame',size=(300,300))
        panel=wx.Panel(self,-1,size=(300,300))
        panel.Bind(wx.EVT_MOTION,self.OnMove)
        wx.StaticText(panel,-1,'pos:',pos=(10,12))
        self.posCtrl=wx.TextCtrl(panel,-1,'',(40,10))
        panel.Bind(wx.EVT_LEFT_DOWN,self.onleftdown)

    def OnMove(self,event):
        pos=event.GetPosition()
        self.posCtrl.SetValue('%s,%s'%(pos.x,pos.y))

    def onleftdown(self, evt):
        print('down')

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame()
    frame.Show(True)
    app.MainLoop()