from subprocess import Popen, PIPE
from playlist import Playlist
from music_crawler import MusicCrawler


class MusicPlayer:

    def __init__(self, name):
        self.playlist = Playlist(name=name, repeat=False, shuffle=False)
        self.process = Popen(["mpg123", ''], stdout=PIPE, stderr=PIPE)
        self.directory = ''

    def play(self, mp3Path):
        process = Popen(["mpg123", mp3Path], stdout=PIPE, stderr=PIPE)
        return process

    def stop(self):
        self.process.kill()

    def add_songs_from_directory(self, directory):
        self.directory = directory
        crawler = MusicCrawler(directory)
        new_playlist = crawler.generate_playlist()

        for song in new_playlist.song_list:
            self.playlist.add_song(song)

    def change_shuffle_mode(self, shuffle):
        self.playlist.shuffle = shuffle

    def change_repeat_mode(self, repeat):
        self.playlist.repeat = repeat

    def show_playlist(self):
        return self.playlist.pprint_playlist()

    def play_next_song(self):
        current_song = self.playlist.next_song()
        full_path = self.directory + '/' + current_song.path
        self.process = self.play(full_path)

        return str(current_song)
