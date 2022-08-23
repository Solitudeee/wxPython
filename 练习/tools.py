import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        text=['a','b','c','d']
        s1=wx.StaticText(self.panel,-1,'下拉框',(10,10))
        wx.Choice(self.panel,-1,pos=(80,10),size=(60,60),choices=text)
        wx.ComboBox(self.panel,-1,pos=(180,10),size=(60,60),choices=text,style=wx.CB_DROPDOWN)

        wx.StaticText(self.panel,-1,'列表框',pos=(10,50))
        wx.ListBox(self.panel,-1,pos=(80,50),size=(60,60),choices=text,style=wx.LB_SINGLE|wx.LB_ALWAYS_SB)

        wx.StaticText(self.panel,-1,'单选框',pos=(170,50))
        panel2=wx.Panel(self.panel,-1,pos=(230,50),size=(100,150))
        wx.RadioButton(panel2,-1,'1',pos=(0,0),style=wx.RB_GROUP)

        wx.StaticText(self.panel,-1,'radiobox',pos=(10,120))
        wx.RadioBox(self.panel,-1,pos=(80,120),size=wx.DefaultSize,choices=text,majorDimension=2,style=wx.RA_SPECIFY_COLS)

        wx.StaticText(self.panel,-1,'复选框列表：',pos=(10,220))
        wx.CheckListBox(self.panel,-1,'RadioBox',pos=(80,120),size=(60,60),choices=text,style=wx.LB_SINGLE|wx.LB_ALWAYS_SB)

        #微调控制器
        wx.StaticText(self.panel,-1,'微调控制器',pos=(190,220))
        sc=wx.SpinCtrl(self.panel,-1,pos=(270,220))
        sc.SetRange(0,4)
        sc.SetValue(2)

        #滑块
        wx.StaticText(self.panel,-1,'滑块',pos=(10,300))
        slider=wx.Slider(self.panel,-1,50,0,100,pos=(70,300),size=(300,30),style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_VALUE_LABEL|wx.SL_LABELS)

        #位图按钮
        wx.StaticText(self.panel,-1,'位图按钮',pos=(10,350))
        bmp=wx.Image('xx.png',wx.BITMAP_TYPE_PNG)
        bmp=wx.Bitmap(bmp.Rescale(20,20))
        wx.BitmapButton(self.panel,-1,bmp,pos=(70,350),style=wx.BORDER_SUNKEN)

        #进度条
        self.count=0
        self.gauge=wx.Gauge(self.panel,-1,100,(70,400),(250,25))

        #消息对话框
        button1=wx.Button(self.panel,-1,'消息对话框',pos=(0,0))
        self.Bind(wx.EVT_BUTTON,self.onClick1,button1)


        def onClick1(self,event):
            dlg1=wx.MessageDialog(self.panel,'Is this the coolest thing ever!','MessageDialog',wx.YES_NO|wx.ICON_QUESTION)
            result=dlg1.ShowModal()
            dlg1.Destory()

        #文本对话框
        button2=wx.Button(self.panel,-1,'文本对话框')


if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()