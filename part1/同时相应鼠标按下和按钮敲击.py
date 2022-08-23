import wx
class DoubleEventFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame with button',size=wx.DefaultSize)
        self.panel=wx.Panel(self,-1)
        self.button=wx.Button(self.panel,-1,'button',pos=(100,13))
        self.Bind(wx.EVT_BUTTON,self.OnButtonClick,self.button)
        self.button.Bind(wx.EVT_LEFT_DOWN,self.OnMouseDown)

    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()

    def OnMouseDown(self,event):
        self.button.SetLabel('Again!')
        event.Skip()

if __name__=='__main__':
    app=wx.PySimpleApp()
    f=DoubleEventFrame(None,-1)
    f.Show()
    app.MainLoop()
