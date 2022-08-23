import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(260, 180))
        self.InitUI()
        # self.Centre()
        self.Show()

    def InitUI(self):
        menuBar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()

        menuBar.Append(filem, "&File")
        menuBar.Append(editm, "&Edit")
        menuBar.Append(helpm, "&Help")
        self.SetMenuBar(menuBar)

        wx.TextCtrl(self)


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Layout1')
    app.MainLoop()