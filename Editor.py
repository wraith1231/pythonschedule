import wx

class ScheduleEditor:
  def __init__(self):
    self.window = wx.Frame(parent=None, title="Schedule Editor", size=wx.Size(500, 700))
    self.window.Show()

  def SetData(self, data:dict):
    # DataManager에게서 받아온 데이터를 화면에 세팅
    pass