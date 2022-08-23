import wx;


class Frame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '复制粘贴例子', size=(500, 300))
        panel = wx.Panel(self)
        self.txt2 = wx.TextCtrl(panel, -1, size=(220, 200), pos=(240, 0), style=wx.TE_MULTILINE)

        self.btn2 = wx.Button(panel, -1, '粘贴文本', size=(60, 30), pos=(260, 210))

        self.Bind(wx.EVT_LEFT_DOWN, self.onleftdown)

        self.txt2.Bind(wx.EVT_LEFT_DOWN,self.onleftdown)


    def onleftdown(self, evt):
        print('down')


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="一对多事件处理", size=(400, 300))
        self.Centre()  # 设置窗口居中

        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)

    def on_left_down(self, event):
        print('鼠标按下')

    def on_left_up(self, event):
        print('鼠标释放')

    def on_mouse_move(self, event):
        print('鼠标移动')
        if event.Dragging() and event.LeftIsDown():
            # 鼠标正在移动，按左键移动
            pos = event.GetPosition()  # 取出位置
            print(pos)


if __name__ == '__main__':
    app = wx.PySimpleApp();
    frame = Frame(None, -1);
    # frame=MyFrame()
    frame.Show();

    app.MainLoop()
