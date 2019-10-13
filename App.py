from flask import Flask, render_template
from youtube_dl_master.youtube_dl import YoutubeDL
from youtube_dl_master.youtube_dl import *

app = Flask(__name__)

ydl_opts ={}

@app.route("/")
def index():
    return render_template('template.html')
"""
def dl_video():
    with YoutubeDL(ydl_opts) as ydl: 
        #ydl.download(['https://www.youtube.com/watch?v=uDjz4FfizuM'])
         ydl.download([zxt])
"""

@app.route('/my-link/')   
def my_link():
    #ydl = YoutubeDL()
    #ydl.add_default_info_extractors()

    #link_of_the_video =input("Copy & paste the URL:")
    #zxt =link_of_the_video.strip()
        #dl_video()
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=uDjz4FfizuM'])
    return 'the download is done'


if __name__ == "__main__":
    app.run(debug=True)
