import wx
import data


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="simple tree", size=(1000, 1000))

        self.li = wx.ImageList(16, 16, True)

        self.a = self.li.Add(wx.Bitmap('1.png', wx.BITMAP_TYPE_PNG))
        self.b = self.li.Add(wx.Bitmap('2.png', wx.BITMAP_TYPE_PNG))
        self.c = self.li.Add(wx.Bitmap('3.png', wx.BITMAP_TYPE_PNG))

        self.a = self.li.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
        self.b = self.li.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, (16, 16)))
        self.c = self.li.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))

        # # create the list control
        # self.list = wx.ListCtrl(self, -1,size=(500,500), style=wx.LC_ICON | wx.LC_AUTOARRANGE)
        # # assign the image list to it
        # self.list.AssignImageList(self.li, wx.IMAGE_LIST_NORMAL)
        # # create some items for the list
        # for x in range(25):
        #     self.list.InsertImageStringItem(self.a,'haha',1)

        # Create the tree
        self.tree = wx.TreeCtrl(self)
        self.tree.AssignImageList(self.li)
        # Add a root node
        root = self.tree.AddRoot("wx.Object")
        self.tree.SetItemImage(root, self.a, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.b, wx.TreeItemIcon_Expanded)

        # Add nodes from our data set
        self.AddTreeNodes(root, data.tree)

        # Bind some interesting events
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated, self.tree)

        # Expand the first level
        self.tree.Expand(root)

        # 获取所有children
        print("所有节点：\n", len(self.getChildren(self.tree, root)))
        print(len(data.tree))

    def AddTreeNodes(self, parentItem, items):
        """
        Recursively traverses the data structure, adding tree nodes to
        match it.
        """
        for item in items:
            if type(item) == str:
                newItem = self.tree.AppendItem(parentItem, item)
                self.tree.SetItemImage(newItem, self.c, wx.TreeItemIcon_Normal)
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.tree.SetItemImage(newItem, self.a, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(newItem, self.b, wx.TreeItemIcon_Expanded)
                self.AddTreeNodes(newItem, item[1])

    def GetItemText(self, item):
        if item:
            return self.tree.GetItemText(item)
        else:
            return ""

    def OnItemExpanded(self, evt):
        print("OnItemExpanded: "), self.GetItemText(evt.GetItem())

    def OnItemCollapsed(self, evt):
        print("OnItemCollapsed:"), self.GetItemText(evt.GetItem())

    def OnSelChanged(self, evt):
        print("OnSelChanged:   "), self.GetItemText(evt.GetItem())

    def OnActivated(self, evt):
        print("OnActivated:    "), self.GetItemText(evt.GetItem())

    # ----------------迭代-------------------------------------------------
    def getChildren(self, tree, parent):
        result = []
        item, cookie = tree.GetFirstChild(parent)
        while item:
            result.append(tree.GetItemText(item))
            item, cookie = tree.GetNextChild(parent, cookie)
        return result


app = wx.PySimpleApp()
frame = TestFrame()
frame.Show()
app.MainLoop()
