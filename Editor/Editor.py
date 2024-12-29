import wx

class ScheduleEditor:
  def __init__(self):
    self.window = wx.Frame(parent=None, title="Schedule Editor", size=wx.Size(500, 700))
    self.window.Show()