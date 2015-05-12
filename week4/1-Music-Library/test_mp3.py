# from mutagen.mp3 import MP3

# f = MP3("08 - Blaze Of Glory.mp3")
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import sys

# from subprocess import Popen, PIPE

# os.ignore("..")

# mp3Path = "Music/Music-Library3"


# def play(mp3Path):
#     p = Popen(["08 - Blaze Of Glory.mp3", mp3Path], stdout=PIPE, stderr=PIPE)
#     return p
# # def stop(process):
# #     process.kill()
# #     p = play("music.mp3")
# #     stop(p)

path = "/home/kostadin/Music/Music-Library"
all_files_in_dir = os.listdir(path)
print (all_files_in_dir)

mp3_files = [mp3 for mp3 in all_files_in_dir if mp3.endswith('mp3')]

# for mp3_file in mp3_files:
#     audio = MP3(mp3_file)
#     print (audio)
#     artist = audio['TPE1']
#     title = audio['TIT2']
#     album = audio['TALB']
#     # length = str(datetime.timedelta(seconds=int(audio.info.length)))

print (mp3_files)
