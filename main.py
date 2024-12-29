import wx
from Editor import Editor
from Timer import Timer

app = wx.App()

editor = Editor.ScheduleEditor()
timer = Timer.ScheduleTimer()

app.MainLoop()