import wx
# import images
class ToolbarFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Toolbars',size=(300,200))
        panel=wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar=self.CreateStatusBar()#1创建状态栏
        
        toolbar=self.CreateToolBar()#2创建工具栏
        images1=wx.Image('xx.png',wx.BITMAP_TYPE_PNG).Rescale(30,30)
        images1=images1.ConvertToBitmap()
        images2=wx.Image('tx.jpg',wx.BITMAP_TYPE_JPEG).Rescale(30,30)
        images2=images2.ConvertToBitmap()
        toolbar.AddSimpleTool(wx.NewId(),images1,"new",'long help for New')#给工具栏增加一个工具
        toolbar.AddSimpleTool(wx.NewId(),images2,'haha','this is a hahaha')
        toolbar.Realize()#准备显示工具栏
        menuBar=wx.MenuBar()#创建菜单栏
        #创建两个菜单
        menu1=wx.Menu()
        menu1.Append(wx.NewId(),'&new','creat a new file')
        menuBar.Append(menu1,"&File")
        menu2=wx.Menu()
        #6 创建菜单的项目
        menu2.Append(wx.NewId(),'&Copy','Copy in status bar')
        menu2.Append(wx.NewId(),'C&ut','')
        menu2.Append(wx.NewId(),'Paste',"")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),'&Options...','Display Options')
        menuBar.Append(menu2,'&Edit')
        self.SetMenuBar(menuBar)
if __name__=="__main__":
    app=wx.PySimpleApp()
    frame=ToolbarFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()