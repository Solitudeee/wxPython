import wx;


class DropTarget(wx.TextDropTarget):
    def __init__(self, object):
        wx.TextDropTarget.__init__(self)
        self.object = object

    def OnDropText(self, x, y, data):
        self.object.AppendText(data)


class Frame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '复制粘贴例子', size=(500, 300))
        panel = wx.Panel(self)
        self.txt1 = wx.TextCtrl(panel, -1, size=(220, 200), pos=(10, 0))
        self.txt2 = wx.TextCtrl(panel, -1, size=(220, 200), pos=(240, 0))
        self.btn1 = wx.Button(panel, -1, '复制文本', size=(60, 30), pos=(20, 210))
        self.btn2 = wx.Button(panel, -1, '粘贴文本', size=(60, 30), pos=(260, 210))

        self.Bind(wx.EVT_BUTTON, self.onDoCopy, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.onDoPaste, self.btn2)
        self.txt1.Bind(wx.EVT_LEFT_DOWN, self.onleftdown)

        dt = DropTarget(self.txt2)
        self.txt2.SetDropTarget(dt)

    def onleftdown(self, evt):
        print('down')
        self.Enable(True)
        self.GetCursor()
        # rg = self.txt1.GetSelection()
        # print(rg)
        # text = self.txt1.GetValue()[rg[0]:rg[1]]
        text = self.txt1.GetValue()
        data = wx.TextDataObject(text)
        dropSource = wx.DropSource(self.txt1)
        dropSource.SetData(data)
        result = dropSource.DoDragDrop(wx.Drag_AllowMove)



    def onDoCopy(self, evt):
        data = wx.TextDataObject()
        data.SetText(self.txt1.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(data)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")

    def onDoPaste(self, evt):
        data = wx.TextDataObject()
        if wx.TheClipboard.Open():
            wx.TheClipboard.GetData(data)
            wx.TheClipboard.Close()
            # self.txt2.SetValue(data.GetText())
            self.txt2.AppendText(data.GetText())
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")


if __name__ == '__main__':
    app = wx.PySimpleApp();
    frame = Frame(None, -1);
    frame.Show();
    app.MainLoop()
