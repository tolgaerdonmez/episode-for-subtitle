import os

subtitles = list()
episodes = list()

file_path = input("file path:")
#video_format = input("video format:")
formats = {".mp4":True,".mkv":True,".avi":True}
video_formats = []
for folder,x,files in os.walk(file_path):
    for file in files:   
        if (file[-4:] == ".srt"):
            subtitles.append(file)
        elif (formats[file[-4:]]):
            video_formats.append(file[-4:])
            episodes.append(file)

# for linux uncomment these next 2 lines \ for windows comment out them
episodes.sort()
subtitles.sort()

print(episodes,"\n",subtitles)
if input("Continue: (y/n) ?") == "y":
    for episode,subtitle,format in zip(episodes,subtitles,video_formats):
        print(file_path + episode,file_path + subtitle[:-4] + format)
        os.rename(file_path + episode,file_path + subtitle[:-4] + format)
    print("Finished")
input("Press any key to quit..")

    
