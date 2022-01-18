import pytube  
from pytube import YouTube 
import os 
os.system('pip3 install pytube')
video_url = input("Enter the link here : ")   
#resolution = input("Enter the resolution : ")
youtube = pytube.YouTube(video_url)  
video = youtube.streams.filter(only_audio=True).first()
print("Starting the Downloads ...............")
video.download() 
print("Download Completed !!")
print("Rename the file extension to mp3 !!")