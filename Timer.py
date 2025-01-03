import wx
import DataManager

class ScheduleTimer:
  def __init__(self, dm:DataManager.DataManager):
    self.window = wx.Frame(parent=None, title="Schedule Timer", size=wx.Size(500, 400))
    self.window.Show()
    self.dm = dm

    self.btnpanel = wx.Panel(self.window, pos=(0, 0), size=(500, 100))
    self.timepanel = wx.Panel(self.window, pos=(0, 100), size=(500, 300))

    self.btns = {}
    self.make_button("Open Editor", 100, 100)
    self.window.Bind(wx.EVT_BUTTON, dm.open_editor, self.btns["Open Editor"])
    self.make_button("Close Timer", 300, 100)
    self.window.Bind(wx.EVT_BUTTON, self.close_timer, self.btns["Close Timer"])

    self.timer_text = wx.TextCtrl(self.timepanel, -1, size=(500, 300))
    self.timer_text.SetValue("Timer")

  def make_button(self, name, pos, size):
    self.btns[name] = wx.Button(self.btnpanel, wx.ID_ANY, name, pos=(pos, 0), size=(size, 100))

  def close_timer(self, point:wx.Point):
    self.window.Close(True)