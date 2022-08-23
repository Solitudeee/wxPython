import wx


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "布局练习")
        panel = wx.Panel(self)

        # 建立控件
        topLbl = wx.StaticText(panel, -1, "账户信息")
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        nameLbl = wx.StaticText(panel, -1, "姓名:")
        name = wx.TextCtrl(panel, -1, "");

        sexLbl = wx.StaticText(panel, -1, "性别:")
        radio1 = wx.RadioButton(panel, -1, '男', style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, -1, '女')

        birthLbl = wx.StaticText(panel, -1, "出生日期：")
        # wx.Choice(self.panel, -1, size=(60, 60), choices=text)
        textY = ['1995', '1996', '1997', '1998', '1999', '2000']
        textM = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        textD = range(1, 31)
        birthY = wx.Choice(panel, -1, choices=textY)
        birthM = wx.Choice(panel, -1, choices=textM)
        birthD = wx.Choice(panel, -1, choices=textM)

        addrLbl = wx.StaticText(panel, -1, "住址:")
        # wx.ComboBox(self.panel, -1, pos=(180, 10), size=(60, 60), choices=text, style=wx.CB_DROPDOWN)
        textS = ['北京', '河南', '陕西']
        textShi = ['某某', '某某']
        combox1 = wx.ComboBox(panel, -1, choices=textS, style=wx.CB_DROPDOWN)
        combox2 = wx.ComboBox(panel, -1, choices=textShi, style=wx.CB_DROPDOWN)

        hobbyLbl = wx.StaticText(panel, -1, "爱好:")
        checkbox1 = wx.CheckBox(panel, -1, '游泳')
        checkbox2 = wx.CheckBox(panel, -1, '滑雪')
        checkbox3 = wx.CheckBox(panel, -1, '看电影')

        heightLbl = wx.StaticText(panel, -1, "身高：")
        slider = wx.Slider(panel, -1, 150, 100, 200,
                           style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_VALUE_LABEL | wx.SL_LABELS)

        # 布局设置

        # mainSizer 最外层布局
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(panel), 0,
                      wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        infoSizer = wx.FlexGridSizer(cols=2, hgap=20, vgap=20)
        infoSizer.AddGrowableCol(1)

        # 姓名
        infoSizer.Add(nameLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        infoSizer.Add(name, 0, wx.EXPAND)

        # 性别
        infoSizer.Add(sexLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sexSizer = wx.BoxSizer(wx.HORIZONTAL)
        sexSizer.Add(radio1, 1)
        sexSizer.Add(radio2, 1)
        infoSizer.Add(sexSizer, 0, wx.EXPAND)

        # 出生日期
        infoSizer.Add(birthLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        birthSizer = wx.BoxSizer(wx.HORIZONTAL)
        birthSizer.Add(birthY, 1)
        birthSizer.Add(wx.StaticText(panel, -1, ' 年'), 1)
        birthSizer.Add(birthM, 1)
        birthSizer.Add(wx.StaticText(panel, -1, ' 月'), 1)
        birthSizer.Add(birthD, 1)
        birthSizer.Add(wx.StaticText(panel, -1, ' 日'), 1)
        infoSizer.Add(birthSizer, 0, wx.EXPAND)

        # 住址
        infoSizer.Add(addrLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer = wx.BoxSizer(wx.HORIZONTAL)
        addrSizer.Add(combox1, 1)
        addrSizer.Add(wx.StaticText(panel, -1, ' 省'), 1)
        addrSizer.Add(combox2, 1)
        addrSizer.Add(wx.StaticText(panel, -1, ' 市'), 1)
        infoSizer.Add(addrSizer, 0, wx.EXPAND)

        # 爱好
        infoSizer.Add(hobbyLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        hobbySizer = wx.BoxSizer(wx.HORIZONTAL)
        hobbySizer.Add(checkbox1, 1)
        hobbySizer.Add(checkbox2, 1)
        hobbySizer.Add(checkbox3, 1)
        infoSizer.Add(hobbySizer, 0, wx.EXPAND)

        # 身高
        infoSizer.Add(heightLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        infoSizer.Add(slider, 0, wx.EXPAND)

        mainSizer.Add(infoSizer, 0, wx.EXPAND | wx.ALL, 10)

        # 按钮
        saveBtn = wx.Button(panel, -1, "保存")
        cancelBtn = wx.Button(panel, -1, "重置")
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(saveBtn)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(cancelBtn)
        btnSizer.Add((20, 20), 1)

        mainSizer.Add(btnSizer, 0, wx.EXPAND | wx.BOTTOM, 10)

        panel.SetSizer(mainSizer)

        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)


app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
