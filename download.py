from youtube_dl_master.youtube_dl import YoutubeDL
from youtube_dl_master.youtube_dl import *



ydl_opts ={}
def dl_video():
    with YoutubeDL(ydl_opts) as ydl: 
        #ydl.download(['https://www.youtube.com/watch?v=uDjz4FfizuM'])
         ydl.download([zxt])
        #ydl.add_default_info_extractors([zxt])

channel =1
while (channel == int(1)):
    link_of_the_video =input("Copy & paste the URL:")
    zxt =link_of_the_video.strip()
    dl_video()
    channel=int(input("enter 1 if you want to download else 0 to quit"))

"""
if __name__ == "__main__":
    app.run(debug=True)
"""