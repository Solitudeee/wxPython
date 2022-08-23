#-*-coding-*-
import wx

class Myframe(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.panel=wx.Panel(self,-1)
        

class app(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        self.version='1'
        self.title=u'我是title'+self.version
        frame=Myframe(None,-1,self.title)
        frame.Show(True)
        return True

if __name__=='__main__':
    a=app()
    a.MainLoop()