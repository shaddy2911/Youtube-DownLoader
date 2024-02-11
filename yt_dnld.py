# import streamlit as st
import os
import re
from pytube import YouTube

class Downloader:
    def __init__(self,URL):
        self.URL=URL

    def video(self):
        yt=YouTube(self.URL)
        directory='Video_Downloads/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        streams=yt.streams.filter(progressive=True,type='video')
        details={}
        details['image']=yt.thumbnail_url
        details['streams']=yt.streams
        details['title']=yt.title
        details['length']=yt.length
        itag, resolutions, vformat, frate = ([] for i in range(4))
        for i in streams:
            res=re.search(r'(\d+)p',str(i))
            res= re.search(r'(\d+)p', str(i))
            typ= re.search(r'video/(\w+)', str(i))
            fps= re.search(r'(\d+)fps', str(i))
            tag= re.search(r'(\d+)',str(i))
            itag.append(str(i)[tag.start():tag.end()])
            resolutions.append(str(i)[res.start():res.end()])
            vformat.append(str(i)[typ.start():typ.end()])
            frate.append(str(i)[fps.start():fps.end()])
        details["resolutions"]= resolutions
        details["itag"]= itag
        details["fps"]= frate
        details["format"]= vformat
        return details

    def audio(self):
        directory='MP3_downloads/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        yt=YouTube(self.URL)
        audio_stream = yt.streams.filter(only_audio=True).first()
        return audio_stream
        
        
        