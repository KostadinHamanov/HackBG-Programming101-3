from subprocess import Popen, PIPE
from playlist import Playlist
from music_crawler import MusicCrawler


class MusicPlayer:

    def __init__(self):
        self.playlist = Playlist(name="NewPlaylist", repeat=False, shuffle=False)
        self.process = Popen(["mpg123", ''], stdout=PIPE, stderr=PIPE)

    def play(self, mp3Path):
        process = Popen(["mpg123", mp3Path], stdout=PIPE, stderr=PIPE)
        return process

    def stop(self):
        self.process.kill()

    def add_songs_from_directory(self, directory):
        crawler = MusicCrawler(directory)
        new_playlist = crawler.generate_playlist()

        for song in new_playlist.song_list:
            self.playlist.add_song(song)

    def change_shuffle(self, shuffle):
        if shuffle is True or shuffle is False:
            self.playlist.shuffle = shuffle

    def change_repeat(self, repeat):
        self.playlist.repeat = repeat

    def show_playlist(self):
        return self.playlist.pprint_playlist()


    def play_next_song(self, directory):
        current_song = self.playlist.next_song()
        full_path = directory + '/' + current_song.name
        self.process = self.play(full_path)


# m = MusicPlayer()
# directory = "/home/kostadin/Music/Music-Library"
# m.add_songs_from_directory(directory)

# print (m.show_playlist())


