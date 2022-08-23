import wx
import data

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, title="Tree")
        self.Center()
        #控件生成
        self.panel=wx.Panel(self,-1,size=(1000,1000))
        self.button = wx.Button(self.panel, -1, '修改', size=(20, 20))
        self.tree=wx.TreeCtrl(self.panel,size=(500, 400),pos=(100,100))

        self.Bind(wx.EVT_BUTTON,self.changeText,self.button)
        #添加根节点
        # root = self.tree.AddRoot(text, image=-1, selImage=-1, data=None)
        # bmp = wx.Image('images/p1.png', wx.BITMAP_TYPE_PNG)
        # bmp = wx.Bitmap(bmp.Rescale(20, 20))
        # bmp2 = wx.Image('images/2.png', wx.BITMAP_TYPE_PNG)
        # bmp2 = wx.Bitmap(bmp2.Rescale(20, 20))
        root=self.tree.AddRoot('wx.Object',data='是根节点')

        #添加其他节点
        self.AddTreeNodes(root,data.tree)

        #绑定事件
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED,self.OnItemExpanded,self.tree)    #该项目以扩展事件
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED,self.OnItemCollapsed,self.tree)  #该项目已折叠
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnSelChanged,self.tree)        #选择已更改
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,self.OnActivated,self.tree)      #该项目已被激活，即通过用鼠标或键盘双击来选择

        self.tree.Expand(root)

    def AddTreeNodes(self,parentItem,items):
        for item in items:
            if type(item)==str:
                self.tree.AppendItem(parentItem,item)
            else:
                newItem=self.tree.AppendItem(parentItem,item[0])
                self.AddTreeNodes(newItem,item[1])

    def GetItemText(self,item):
        if item:
            return self.tree.GetItemText(item)
        else:
            return ""
    def OnItemExpanded(self,evt):
        print('OnItemExpand')
        self.GetItemText(evt.GetItem())
    def OnItemCollapsed(self,evt):
        print('OnItemCollapsed')
        self.GetItemText(evt.GetItem())

    def OnSelChanged(self,evt):
        print("OnselChanged")
        self.GetItemText(evt.GetItem())

    def OnActivated(self,evt):
        print('OnActivated')
        self.GetItemText(evt.GetItem())

    def changeText(self,event):
        item=self.tree.GetFirstChild(self.tree.GetRootItem())[0]
        print(item)
        self.tree.SetItemText(item,'修改了')



app=wx.PySimpleApp()
frame=MyFrame()
frame.Show()

app.MainLoop()