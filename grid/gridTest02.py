import wx
import wx.grid

class MyGridTableBase(wx.grid.PyGridTableBase):
    def __init__(self):
        wx.grid.PyGridTableBase.__init__(self)
        self.data={
            (1,1):'one',
            (2,2):'two',
            (3,3):'three',
            (4,4):'four'

        }

    def GetNumberCols(self):
        return 20
    def GetNumberRows(self):
        return 20
    def GetValue(self,row,col):
        value=self.data.get((row,col))
        if value is not None:
            return value
        else :
            return ''
    def IsEmptyCell(self, row, col):
        return self.data.get((row,col)) is not None
    def SetValue(self, row, col, value):
        self.data[(row,col)]=value

    def AppendRows(self,numRows=1):
        print('hello')
        return True




class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title="Simple Grid",size=(600,600))
        self.panel=wx.Panel(self,-1,size=(600,600))
        self.bt1=wx.Button(self.panel,-1,'确定',size=(30,20),pos=(5,5))
        self.Bind(wx.EVT_BUTTON,self.onClick,self.bt1)
        self.bt2 = wx.Button(self.panel, -1, '确定', size=(30, 20), pos=(5, 35))
        self.Bind(wx.EVT_BUTTON, self.onClick, self.bt2)

        self.grid=wx.grid.Grid(self.panel,-1,size=(400,400),pos=(50,5))
        # self.grid.CreateGrid(20,20,selmode=wx.grid.Grid.GridSelectCells)
        table=MyGridTableBase()
        self.grid.SetTable(table,True)


    def onClick(self,event):
        obj=event.GetEventObject()
        if obj is self.bt1:
            print(self.grid.GetNumberCols(),self.grid.GetNumberRows())
            self.grid.SetCellValue(1,2,'wao')
        elif obj is self.bt2:
            self.grid.AppendRows(numRows=1)

app=wx.PySimpleApp()
frame=MyFrame()
frame.Show()
app.MainLoop()