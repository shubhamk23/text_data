
from pytube import YouTube
from pytube import Playlist
import os

class Download_Video:
    def Download(self, link, path):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download(path)
        except:
            print("An Error has occured")
        print("Download is completed successfully")
        return 
    
    def title_video(self, link):
        youtubeObject = YouTube(link)
        return youtubeObject.title
    
    def thumbnail_url(self, link):
        youtubeObject = YouTube(link)
        return youtubeObject.thumbnail_url

    def get_playlist_urls(self, playlist_url):
        playlist = Playlist(playlist_url)
        return playlist.video_urls
    
    def delete_files_in_directory(self, directory_path):
        try:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                print("All files deleted successfully.")
        except OSError:
            print("Error occurred while deleting files.")


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

