import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        bmp=wx.Image('02.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        self.button=wx.BitmapButton(self.panel,-1,bmp,pos=(10,20),style=wx.BORDER_SUNKEN)
        # self.button.SetDefault()



        bmp2=wx.Image('01.png',wx.BITMAP_TYPE_PNG)
        bmp2=wx.Bitmap(bmp2.Rescale(20,20))

        self.button2=wx.BitmapButton(self.panel,-1,bmp2,pos=(10,200),style=wx.BORDER_NONE)

        self.button3=wx.ToggleButton(self.panel,-1,'ToggleButton',pos=(10,300))


if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()