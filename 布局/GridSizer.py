import wx


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self, -1, size=(700, 500))
        sizer = wx.GridSizer(4, 3, 5, 5)

        text = "a b c d e f g"
        text = text.split()
        for x in text:
            txt = wx.Button(panel, -1, x)
            sizer.Add(txt, 0, wx.ALL, 10)

        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()

    frame = MyFrame(None)
    frame.Show()

    app.MainLoop()
