import wx
import Editor
import Timer

app = wx.App()

editor = Editor.ScheduleEditor()
timer = Timer.ScheduleTimer()


app.MainLoop()