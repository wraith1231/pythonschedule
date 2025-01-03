import wx
import json
import Timer
import Editor

class DataManager:
  def __init__(self):
    self.window = wx.Frame(parent=None, title="File Loader")

    try:
      f = open("Data/info.json", "r")
      json_data = json.load(f)
      current_file = json_data["current_file"]

    except FileNotFoundError:
      data = {}
      data["current_file"] = "None"
      current_file = "None"
      f = open("Data/info.ini", "w")
      json.dump(data, f)
    
    self.editor = Editor.ScheduleEditor()

    if current_file != "None":
      try:
        # editor에 불러온 파일에서 뽑아온 데이터 전달
        pass

      except FileNotFoundError:
        # self.SelectFile()
        pass

    else:
      # self.SelectFile()
      pass

  def SelectFile(self):
    sf = wx.FileDialog(
      self.window, 
      "Load File",
      wildcard="Json Files (*.json)|*.json",
      style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    if sf.ShowModal() == wx.ID_CANCEL:
      # editor에 기본 설정 불러오도록 안내
      pass
    
    path = sf.GetPath().split(".")
    extention = path[len(path)-1]
    if extention != "json":
      wx.LogWarning("Select Wrong Schedule!!")
    else:
      # 처음엔 무한 반복 시켰는데 요러면 상태가 요상해서 그냥 빈 데이터로 하는걸로 함
      return False
    # 파일 정상적으로 선택했으면 데이터 넘겨야지
    return True
    
      
  def open_editor(self, btn:wx.Point):
    self.editor.show_window()
    pass

  def LoadData(self):
    return self.current_data
  
  def SaveData(self, data:dict):
    pass

      
    
