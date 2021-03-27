# -----------------------使用pygame库播放音乐-----------------------开始
from pygame import mixer
import time

mixer.init()
mixer.music.load('xx.mp3')
mixer.music.play()
time.sleep(50)  # 播放50秒
mixer.music.stop()
# -----------------------使用pygame库播放音乐-----------------------结束
