import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        text = ['a', 'b', 'c', 'd']
        lb=wx.ListBox(self.panel,-1,pos=(50,50),size=(60,60),choices=text,style=wx.LB_SINGLE|wx.LB_ALWAYS_SB)




if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()