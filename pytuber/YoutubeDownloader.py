from pytube import YouTube

def Download (link):
    youtubeObject=YouTube(link)
    youtubeObject= youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred!")
    print("Download successful :) ") 
link= input("Enter the Youtube video url: ")
Download(link)
