import wx
class Example(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent,title=title,size=(300,200))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        p = wx.Panel(self)
        gs = wx.GridSizer(4, 4, 5, 5)
        for i in range(1, 17):
            btn = "Btn" + str(i)
            gs.Add(wx.Button(p, label=btn), 0, wx.EXPAND)
            p.SetSizer(gs)#把GridSizer与框架关联起来


app = wx.PySimpleApp()
Example(None, title='Grid Demo - www.yiibai.com')
app.MainLoop()