import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)


        self.radio1=wx.RadioButton(self.panel,-1,'1',pos=(10,100),style=wx.RB_GROUP)
        self.radio2=wx.RadioButton(self.panel,-1,'2',pos=(10,120))
        self.radio3=wx.RadioButton(self.panel,-1,'3',pos=(10,140))

        self.text1=wx.TextCtrl(self.panel,-1,'',pos=(60,100))
        self.text2=wx.TextCtrl(self.panel,-1,'',pos=(60,120))
        self.text3=wx.TextCtrl(self.panel,-1,'',pos=(60,140))

        self.texts={'1':self.text1,'2':self.text2,'3':self.text3}
        for eachText in [self.text2,self.text3]:
            eachText.Enable(False)
        for eachRadio in [self.radio1,self.radio2,self.radio3]:
            self.Bind(wx.EVT_RADIOBUTTON,self.OnRadio,eachRadio)
        self.selectedText=self.text1

    def OnRadio(self,event):
        if self.selectedText:
            self.selectedText.Enable(False)
        radioSelected = event.GetEventObject()
        print(self.texts[radioSelected.GetLabel()])
        text = self.texts[radioSelected.GetLabel()]
        text.Enable(True)
        self.selectedText = text



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()