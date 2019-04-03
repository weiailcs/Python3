# -*- coding: utf-8 -*-

import wx


class GuageFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(500, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 100, (100, 50), (300, 30))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Center(True)

    def OnIdle(self, event):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)
        if self.count >= 92:
            self.Close()


if __name__ == '__main__':
    app = wx.App()
    frame = GuageFrame()
    frame.Show()
    app.MainLoop()
