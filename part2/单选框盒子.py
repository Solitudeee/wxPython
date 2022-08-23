import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)

        text=['a','b','c','d']
        self.rb=wx.RadioBox(self.panel,-1,'RadioBox',pos=(50,50),size=wx.DefaultSize,choices=text,majorDimension=2,style=wx.RA_SPECIFY_COLS)

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