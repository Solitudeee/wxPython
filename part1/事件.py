import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'各种事件',size=(600,600))
        self.panel=wx.Panel(self)
        #弹窗按钮
        self.button=wx.Button(self.panel,-1,'按钮',pos=(0,0))
        self.Bind(wx.EVT_BUTTON,self.onClick,self.button)
        #关闭按钮
        button1 = wx.Button(self.panel, -1,'Close', pos = (130, 15),size = (40, 40))
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button1)
        #设置菜单
        self.menubar=wx.MenuBar()
        menu1=wx.Menu()
        menuItem=menu1.Append(-1,'&exit...')
        self.menubar.Append(menu1,'&File')
        self.SetMenuBar(self.menubar)
        self.Bind(wx.EVT_MENU,self.OnCloseMe,menuItem)

    def OnCloseMe(self, event):
            print('close me')
            self.Close(True)


    def OnCloseWindow(self, event):
            print('destory me')
            self.Destroy()

    def onClick(self,event):
        dlg=wx.MessageDialog(self.panel,'发生了什么',caption='MessageBox',style=wx.OK|wx.CANCEL,pos=wx.DefaultPosition)
        dlg.ShowModal()
        # dlg.Destroy()


if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,-1)
    frame.Show()
    app.MainLoop()
