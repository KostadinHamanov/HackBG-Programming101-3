import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from playlist import Playlist
from song import Song
import datetime


class MusicCrawler:

    def __init__(self, path):
        self.path = path
        self.music_files = [
            song for song in os.listdir(self.path) if song.endswith('.mp3')]

    def generate_playlist(self):
        playlist = Playlist(name="NewPlaylist", repeat=False, shuffle=False)

        for music_file in self.music_files:
            audio = MP3(self.path + '/' + music_file, ID3=EasyID3)
            artist = audio['artist'][0]
            title = audio['title'][0]
            album = audio['album'][0]
            length = str(datetime.timedelta(seconds=int(audio.info.length)))

            song = Song(title=title, artist=artist,
                        album=album, length=length)

            playlist.add_song(song)

            song.path = music_file

        return playlist
