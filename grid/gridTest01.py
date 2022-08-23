import wx
import wx.grid
import wx.grid.GridEvent
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title="Simple Grid",size=(900,600))
        self.panel=wx.Panel(self,-1,size=(900,600))
        self.bt1=wx.Button(self.panel,-1,'确定',size=(30,20),pos=(5,5))
        self.Bind(wx.EVT_BUTTON,self.onClick,self.bt1)
        self.bt2 = wx.Button(self.panel, -1, '添加一行', size=(60, 20), pos=(5, 35))
        self.Bind(wx.EVT_BUTTON, self.onClick, self.bt2)
        self.bt3 = wx.Button(self.panel, -1, '状态判断', size=(60, 20), pos=(5, 65))
        self.Bind(wx.EVT_BUTTON, self.onClick, self.bt3)
        self.bt4 = wx.Button(self.panel, -1, '单元格可见', size=(70, 20), pos=(5, 95))
        self.Bind(wx.EVT_BUTTON, self.onClick, self.bt4)

        self.grid=wx.grid.Grid(self.panel,-1,size=(600,400),pos=(150,5))
        self.grid.CreateGrid(20,20,selmode=wx.grid.Grid.GridSelectCells)
        self.Bind(wx.EVT_GRID_CELL_LEFT_CLICK,self.leftClickOnGrid,self.grid)
        for i in range(20):
            self.grid.SetRowLabelValue(i,str(i))
            self.grid.SetColLabelValue(i,str(i))

    def onClick(self,event):
        obj=event.GetEventObject()
        if obj is self.bt1:
            print(self.grid.GetNumberCols(),self.grid.GetNumberRows())
            self.grid.SetCellValue(1,2,'wao')
        elif obj is self.bt2:
            self.grid.AppendRows(numRows=1)
        elif obj is self.bt3:
            print('是否有被选中的单元格',self.grid.IsSelection())
            print('2,3格是否被选中',self.grid.IsInSelection(2,3))
            print('GetSelectedCells:',self.grid.GetSelectedCells())
            print('GetSelectedCols:',self.grid.GetSelectedCols())
            print('GetSelectedRows:',self.grid.GetSelectedRows())
            print('GetSelectionBlockTopLeft:',self.grid.GetSelectionBlockTopLeft())
            print('GetSelectionBlockBottomRight:',self.grid.GetSelectionBlockBottomRight())
        elif obj is self.bt4:
            print('（19,19）是否可见：',self.grid.IsVisible(19,19,False))
            self.grid.MakeCellVisible(19,19)
            self.grid.SelectBlock(19,19,19,19)
            print(self.grid.BlockToDeviceRect((1,1),(5,5)))
    def leftClickOnGrid(self,event):
        a=event.AltDown()
        print(a)



app=wx.PySimpleApp()
frame=MyFrame()
frame.Show()

app.MainLoop()