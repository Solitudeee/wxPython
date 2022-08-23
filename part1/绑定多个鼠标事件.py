import wx
class MouseEventFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame With Button',size=(300,100))
        self.panel=wx.Panel(self)
        self.button=wx.Button(self.panel,label='NOT over',pos=(100,15))
        # self.button.SetEvtHandlerEnabled(False)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClick,self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW,self.OnEnterWindow)
        self.button.Bind(wx.EVT_LEAVE_WINDOW,self.OnLeaveWindow)

    def OnButtonClick(self,event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()
        event.Skip()

    def OnEnterWindow(self,event):
        self.button.SetLabel('Over me!')
        event.Skip()

    def OnLeaveWindow(self,event):
        self.button.SetLabel('Not Over!')
        event.Skip()

if __name__ =='__main__':
    app=wx.PySimpleApp()
    frame=MouseEventFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()