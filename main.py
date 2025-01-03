import wx
import Editor
import Timer
import DataManager

app = wx.App()

# editor = Editor.ScheduleEditor()
dm = DataManager.DataManager()
timer = Timer.ScheduleTimer(dm)

app.MainLoop()