import wx
import time
import os

cwd=os.getcwd()
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'设置图标样例',size=(500,500))
        self.panel=wx.Panel(self)

        self.buttonOK=wx.Button(self.panel,-1,'OK',(20,20),(60,30))
        self.Bind(wx.EVT_BUTTON,self.Onclick,self.buttonOK)

        self.buttonCancel=wx.Button(self.panel,-1,'Cancel',(20,80),(60,30))
        self.Bind(wx.EVT_BUTTON,self.Onclick,self.buttonCancel)


        #设置菜单栏
        menuBar = wx.MenuBar()  # 创建菜单栏
        menu1 = wx.Menu()
        menu1.Append(wx.NewId(), '&new', 'creat a new file')
        item=menu1.Append(wx.NewId(),'&Exit','退出')
            #绑定事件
        self.Bind(wx.EVT_MENU,self.onExit,item)
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        # 6 创建菜单的项目
        menu2.Append(wx.NewId(), '&Copy', 'Copy in status bar')
        menu2.Append(wx.NewId(), 'C&ut', '')
        menu2.Append(wx.NewId(), 'Paste', "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), '&Options...', 'Display Options')
        menuBar.Append(menu2, '&Edit')
        self.SetMenuBar(menuBar)

        self.setUpIcon()




    def onExit(self,event):
        self.Destroy()
    def setUpIcon(self):
        self.imag_path=os.path.abspath('./xx.png')
        icon=wx.Icon(self.imag_path,type=wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)


    def Onclick(self,event):
        if event.GetEventObject()==self.buttonOK:
            print("{}".format(event.GetEventObject().GetLabel()))

        if event.GetEventObject()==self.buttonCancel:
            print('cancel')




class app(wx.App):
    def OnInit(self):
        f=MyFrame(None,-1)
        f.Show(True)
        return True
if __name__=='__main__':
    a=app()
    a.MainLoop()