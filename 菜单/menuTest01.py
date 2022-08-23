import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title="菜单栏测试",size=(300,300))

        menuBar=wx.MenuBar()
        menu1=wx.Menu()
        menu2=wx.Menu()
        menu3=wx.Menu()
        menu4=wx.Menu()
        menu5=wx.Menu()
        menuBar.Append(menu1,'文件')
        menuBar.Insert(0,menu2,'第一个')
        menuBar.Remove(0)
        m1=menu1.Append(-1,"打开","正在打开文件",kind=wx.ITEM_NORMAL)
        bmp=wx.Bitmap('02.ico',wx.BITMAP_TYPE_ICO)
        m1.SetBitmap(bmp)
        self.Bind(wx.EVT_MENU,self.onOpen,m1)




        self.SetMenuBar(menuBar)

    def onOpen(self,event):
        print("打开一个文件")



if __name__ == '__main__':
   app=wx.PySimpleApp()
   frame=MyFrame()
   frame.Show()
   app.MainLoop()