import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'dialog',size=(300,300))
        self.panel=wx.Panel(self)
        self.panel.SetBackgroundColour('white')
        button1=wx.Button(self.panel,-1,'消息对话框',pos=(0,0))
        button2=wx.Button(self.panel,-1,'文本对话框',pos=(100,0))
        button3=wx.Button(self.panel,-1,'列表对话框',pos=(200,0))
        self.Bind(wx.EVT_BUTTON,self.onclick1,button1)
        button2.Bind(wx.EVT_BUTTON,self.onclick2)
        button3.Bind(wx.EVT_BUTTON,self.onclick3)
        self.text=wx.TextCtrl(self.panel,size=(200,100),pos=(50,100))
    #消息对话框
    def onclick1(self,event):
        dlg1 = wx.MessageDialog(self.panel, "Is this the coolest thing ever!", 'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg1.ShowModal()
        dlg1.Destroy()
        if result==wx.ID_YES:
            self.text.AppendText(str(result))
    #文本对话框
    def onclick2(self,event):
        dlg2=wx.TextEntryDialog(self.panel,"Who is burid in Grant's tomb?",'A question','CaryGrant')
        if dlg2.ShowModal()==wx.ID_OK:
            response=dlg2.GetValue()
            self.text.AppendText(response)
    #列表对话框
    def onclick3(self,event):
        dlg3=wx.SingleChoiceDialog(self.panel,'What version of Python are you using?','single choice',['1.5.2','2.0','2.1.3','2.2'])
        if dlg3.ShowModal()==wx.ID_OK:
            response=dlg3.GetStringSelection()
            self.text.AppendText(response)
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,id=wx.NewId())
    frame.Show()
    app.MainLoop()