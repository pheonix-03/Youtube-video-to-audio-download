import pytube  
from pytube import YouTube 
import os 
os.system('pip3 install pytube')
video_url = input("Enter the link here : ")   
youtube = pytube.YouTube(video_url)  
video = youtube.streams.filter(only_audio=True).first()
print(video)
print("Starting the Downloads ...............")
x = video.download()
xnew = "music.mp4"
os.rename(x,xnew)
os.system('ffmpeg -i '+str(xnew)+" "+str("music")+'.'+'mp3')
os.remove(xnew)
print("Download Completed !!")
#print("Rename the file extension!!")
