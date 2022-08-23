import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        wx.CheckBox(self.panel,-1,'A',pos=(10,20))
        wx.CheckBox(self.panel,-1,'B',pos=(10,40))
        wx.CheckBox(self.panel,-1,'C',pos=(10,60))

        wx.RadioButton(self.panel,-1,'1',pos=(10,100))
        wx.RadioButton(self.panel,-1,'2',pos=(10,120))
        wx.RadioButton(self.panel,-1,'3',pos=(10,140))




if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()