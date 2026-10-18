# convert the videos into mp3
import os
import subprocess

files = os.listdir("videos")

for file in files:
    video_num = file.split(". ")[0]
    video_name = file.split(". ")[1].split(".")[0]
    print(video_num, video_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{video_num}_{video_name}.mp3"])