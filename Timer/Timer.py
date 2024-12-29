import wx

class ScheduleTimer:
  def __init__(self):
    self.window = wx.Frame(parent=None, title="Schedule Timer", size=wx.Size(500, 500))
    self.window.Show()