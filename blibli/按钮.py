# -*-coding-*-
import wx


class Myframe(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, -1)
        self.button1=wx.Button(self.panel,-1,'button1',pos=(100,15))
        self.Bind(wx.EVT_BUTTON,self.onClick,self.button1)

        self.button2=wx.Button(self.panel,-1,'button2',pos=(100,40))
        self.Bind(wx.EVT_BUTTON,self.onClick,self.button2)




    def onClick(self,event):
        if event.GetEventObject()==self.button1:
            print("{}".format(event.GetEventObject().GetLabel()))
        if event.GetEventObject()==self.button2:
            print("{}".format(event.GetEventObject().GetLabel()))


class app(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        self.version = '1'
        self.title = u'我是title' + self.version
        frame = Myframe(None, -1, self.title)
        frame.Show(True)
        return True


if __name__ == '__main__':
    a = app()
    a.MainLoop()