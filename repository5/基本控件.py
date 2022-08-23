import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本')
        self.panel=wx.Panel(self)
        text = ['a', 'b', 'c', 'd']
        #下拉框
        s1=wx.StaticText(self.panel,-1,'下拉框：',pos=(10,10))

        wx.Choice(self.panel,-1,pos=(80,10),size=(60,60),choices=text)
        wx.ComboBox(self.panel, -1, pos=(180, 10), size=(60, 60), choices=text, style=wx.CB_DROPDOWN)

        #列表框
        s2 = wx.StaticText(self.panel, -1, '列表框：', pos=(10, 50))
        lb = wx.ListBox(self.panel, -1, pos=(80, 50), size=(60, 60), choices=text, style=wx.LB_SINGLE | wx.LB_ALWAYS_SB)

        #单选按钮
        s2 = wx.StaticText(self.panel, -1, '单选按钮：', pos=(170, 50))
        panel2=wx.Panel(self.panel,-1,pos=(230,50),size=(100,150))
        self.radio1 = wx.RadioButton(panel2, -1, '1', pos=(0, 0), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel2, -1, '2', pos=(0, 20))
        self.radio3 = wx.RadioButton(panel2, -1, '3', pos=(0, 40))

        self.text1 = wx.TextCtrl(panel2, -1, '', pos=(40, 0))
        self.text2 = wx.TextCtrl(panel2, -1, '', pos=(40, 20))
        self.text3 = wx.TextCtrl(panel2, -1, '', pos=(40, 40))

        self.texts = {'1': self.text1, '2': self.text2, '3': self.text3}
        for eachText in [self.text2, self.text3]:
            eachText.Enable(False)
        for eachRadio in [self.radio1, self.radio2, self.radio3]:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)
        self.selectedText = self.text1

        #radioBox
        wx.StaticText(self.panel, -1, 'radioBox：', pos=(10, 120))
        self.rb = wx.RadioBox(self.panel, -1, 'RadioBox', pos=(80, 120), size=wx.DefaultSize, choices=text,
                              majorDimension=2, style=wx.RA_SPECIFY_COLS)

        #复选框列表
        wx.StaticText(self.panel, -1, '复选框列表：', pos=(10, 220))
        wx.CheckListBox(self.panel, -1, pos=(100, 220), size=(60, 60), choices=text,
                             style=wx.LB_SINGLE | wx.LB_ALWAYS_SB)

        #微调控制器
        wx.StaticText(self.panel, -1, '微调控制器：', pos=(190, 220))
        sc = wx.SpinCtrl(self.panel, -1,pos=(270,220),style=wx.SP_ARROW_KEYS|wx.ALIGN_CENTER_HORIZONTAL)
        sc.SetRange(0, 4)
        sc.SetValue(2)

        #滑块
        wx.StaticText(self.panel, -1, '滑块：', pos=(10, 300))
        slider = wx.Slider(self.panel, -1, 50, 0, 100, pos=(70, 300), size=(300, 30),
                           style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_VALUE_LABEL | wx.SL_LABELS)
        slider.SetTickFreq(5)

        #位图按钮
        wx.StaticText(self.panel, -1, '位图按钮：', pos=(10, 350))
        bmp = wx.Image('xx.png', wx.BITMAP_TYPE_PNG)
        bmp = wx.Bitmap(bmp.Rescale(20, 20))
        self.button = wx.BitmapButton(self.panel, -1, bmp, pos=(70, 350), style=wx.BORDER_SUNKEN)

        #进度条
        wx.StaticText(self.panel, -1, '进度条：', pos=(10, 400))
        self.count = 0
        self.gauge = wx.Gauge(self.panel, -1, 100, (70, 400), (250, 25),style=wx.GA_TEXT)
        self.Bind(wx.EVT_IDLE, self.OnIdle)


    def OnIdle(self, event):
        self.count = self.count + 1
        if self.count >= 500:
            self.count = 0
        self.gauge.SetValue(self.count)

    def OnRadio(self,event):
        if self.selectedText:
            self.selectedText.Enable(False)
        radioSelected = event.GetEventObject()
        print(self.texts[radioSelected.GetLabel()])
        text = self.texts[radioSelected.GetLabel()]
        text.Enable(True)
        self.selectedText = text




if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()