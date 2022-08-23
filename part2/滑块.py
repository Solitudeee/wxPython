import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        slider=wx.Slider(self.panel,-1,50,0,100,pos=(50,50),size=(400,30),style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_VALUE_LABEL|wx.SL_LABELS)
        slider.SetTickFreq(5)

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()