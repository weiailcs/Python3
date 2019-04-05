import wx
import time
import _thread


class GuageFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(500, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 10, (50, 50), (300, 20))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        # 进度条自身绑定循环任务，监听进度
        self.gauge.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Center(True)

    def OnIdle(self, event):
        self.gauge.SetValue(self.count)
        if self.count == 10:
            # 到达计划进度，取消进度条
            self.Destroy()

    def timer(self, no, interval):
        while self.count < 10:
            time.sleep(interval)
            self.count += 1


if __name__ == '__main__':
    app = wx.App()
    frame = GuageFrame()
    frame.Show()
    # 创建线程，设定延迟加载时间及间隔执行时间
    _thread.start_new_thread(frame.timer, (0.5, 0.2))
    app.MainLoop()
