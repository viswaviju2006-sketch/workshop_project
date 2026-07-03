import streamlit as st
import os
import glob

#Handling MoviePy version difference (v1.x vs v2.x)
try:
  from moviepy.editor import ImageClip ,concatenate_videoclips,AudioFileClip
except ImportError:
  from moviepy import ImageClip, concatenate_videoclips,AudioFileClip
import yt_dlp

#---1,INITIALIZE STATE---
if 'audio_path' not in st.session_state:
  st.session_state['audio_path'] = None
  if'yt_error' in st.session_state:
    pass # keep it for display logic

#---2, DEFINE ALL FUNCTIONS---

def cleanup_temp_files():
  """Removes temporary files and resets memory,"""
  files + glob.glob("temp_*") + ["output_video.mp4"]
  for f in files:
    try:
        os.remove(f)
    except:
        pass
  st.session_state['audio_path'] = None
  if 'yt_error' in st.session_state:
    del st.session_state['yt_error']

def download_youtube_audio(url):
  """Downloads only audio from YouTube using reliable browser impersonation."""
audio_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'temp_audio.%(ext)s',
    'http_headers':{
         'User_Agent': "Mozilla/5.0 (Windows NT 10/0; win64; x64) ApplewebKit/537.36 (KHTML,like Gecko) Chrome/122.0.0.0 Safari/537.36',
         'Accept': "https://www.gppgle.com/',
    },
    'postprocessors': [{
        'key': 'FfmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
with yt_dlp.YoutubeDL(audio_opts) as ydl
    ydl.download([url])
return "temp_audio.mp3"

def handle_youtube__download(url):
    """Callback function to ensure session state persists
      
