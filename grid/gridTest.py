import wx
import wx.grid
# wx.grid.Grid(parent,id,pos=wx.DefaultPosition,size=wx.DefaultSize,style=wx.WANTS_CHARS,name=wxPanelNameStr)

# class SimpleGrid(wx.grid.Grid):
#     def __init__(self,parent):
#         wx.gird.Grid(9,2)
#         self.SetColLabelValue(0,'First')

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,None,title='Simple Grid',size=(640,480))
        grid=wx.grid.Grid(self)
        grid.CreateGrid(50,50)
        for row in range(20):
            for col in range(6):
                grid.SetCellValue(row,col,'cell(%d,%d)'%(row,col))

app=wx.PySimpleApp()
frame=MyFrame()
frame.Show()

app.MainLoop()