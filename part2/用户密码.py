import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        # text=wx.StaticText(self.panel,-1,'我是文本框\n''woshi ',(100,50),(160,-1),style=wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ST_ELLIPSIZE_END|wx.BORDER_SUNKEN)
        # #字体大小，Family，风格，粗细,下划线,
        # font=wx.Font(18,wx.FONTFAMILY_TELETYPE,wx.FONTSTYLE_NORMAL,700,False)
        # text.SetFont(font)
        basicLabel=wx.StaticText(self.panel,-1,'Basic Control:')
        basicText=wx.TextCtrl(self.panel,-1,'I have enter some text')
        basicText.SetInsertionPoint(0)
        pwdLabel=wx.StaticText(self.panel,-1,'password:')
        pwdText=wx.TextCtrl(self.panel,-1,style=wx.TE_PASSWORD)
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basicLabel,basicText,pwdLabel,pwdText])
        self.panel.SetSizer(sizer)




if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()