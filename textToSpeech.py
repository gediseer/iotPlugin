from miio import WifiSpeaker

  
# 创建一个设备对象  
speaker = WifiSpeaker("192.168.110.60", "34785a543141464f626e33394a596363")  
  
# 获取设备的状态  
state = speaker.status()  
  
# 检查设备的播放状态  
# if state.play_state == PlayState.Playing:  
#     print("音箱正在播放音乐")  
  
# 播放文字  
speaker.play_text("欢迎使用智能家居系统")  