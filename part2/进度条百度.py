#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
class GuageFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(600, 300))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 100, (100, 60), (250, 25))
        # self.gauge.SetBezelFace(3)
        # self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

    def OnIdle(self, event):
        self.count = self.count + 1
        if self.count >= 80:
            self.count = 0
        self.gauge.SetValue(self.count)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = GuageFrame()
    frame.Show()
    app.MainLoop()