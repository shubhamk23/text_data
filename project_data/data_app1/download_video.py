
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

# # Initialize the object 
# obj1 = Download_Video()

# # Define the parameters
# # playlist_url = "https://wz1cgxiH5KCBsyQij1HsPtGww.youtube.com/playlist?list=PL0b6OzIxLPb"
# playlist_url = "https://www.youtube.com/playlist?list=PLVBKjEIdL9bsgfTLn9AihqIKXYH8y33cS"
# save_path = "testing_video"

# # Checking the url playlist
# list_url = obj1.get_playlist_urls(playlist_url)

# print(list_url)
# # cleaning the spaces inside url
# list_url = [url.strip() for url in list_url]

# print('Number Of Videos In playlist: %s' % len(list_url))

# for index, url in enumerate(list_url):
#     print(str(index+1)+") "+ url)

#     # here strip is required to pass clean url
#     obj1.Download(url, save_path)
