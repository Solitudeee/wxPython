import wx
import data1


class TreeFrame(wx.TreeCtrl):
    def __init__(self,parent):
        wx.TreeCtrl.__init__(self,parent)

    def OnCompareItems(self, item1, item2):
        data1 = self.GetItemData(item1)
        data2 = self.GetItemData(item2)
        if data1 < data2:
            return -1
        elif data1 > data2:
            return 1
        else:
            return 0


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="simple tree", size=(400, 500))

        # Create the tree
        self.tree = TreeFrame(self)

        # Add a root node
        root = self.tree.AddRoot("wx.Object")

        # Add nodes from our data set
        self.AddTreeNodes(root, data1.tree,data1.datas)

        # Bind some interesting events
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated, self.tree)

        # Expand the first level
        self.tree.Expand(root)
        self.tree.SortChildren(root)
    def AddTreeNodes(self, parentItem, items,datas):
        """
        Recursively traverses the data structure, adding tree nodes to
        match it.
        """
        # for item in items:
        #     if type(item) == str:
        #         self.tree.AppendItem(parentItem, item)
        #     else:
        #         newItem = self.tree.AppendItem(parentItem, item[0])
        #         self.AddTreeNodes(newItem, item[1])

        for i in range(len(items)):
            if type(items[i])==str:
                print(items[i])
                self.tree.AppendItem(parentItem, text=items[i],data=datas[i])
            else:
                newItem=self.tree.AppendItem(parentItem,text=items[i][0],data=datas[i][0])
                self.AddTreeNodes(newItem,items[i][1],datas[i][1])



    def GetItemText(self, item):
        if item:
            return self.tree.GetItemText(item)
        else:
            return ""

    def OnItemExpanded(self, evt):
        print("OnItemExpanded: ",self.tree.GetItemPyData(evt.GetItem()))
        self.GetItemText(evt.GetItem())

    def OnItemCollapsed(self, evt):
        print("OnItemCollapsed:")
        self.GetItemText(evt.GetItem())

    def OnSelChanged(self, evt):
        print("OnSelChanged:   ")
        self.GetItemText(evt.GetItem())

    def OnActivated(self, evt):
        print("OnActivated:    ")
        self.GetItemText(evt.GetItem())


app = wx.PySimpleApp()
frame = TestFrame()
frame.Show()
app.MainLoop()
