import wx
import Editor
import Timer
import DataManager

app = wx.App()

# editor = Editor.ScheduleEditor()
timer = Timer.ScheduleTimer()
dm = DataManager.DataManager()

app.MainLoop()