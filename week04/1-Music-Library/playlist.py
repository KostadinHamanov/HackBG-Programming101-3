import random
import json
from tabulate import tabulate
from song import Song
import time


class Playlist:

    def __init__(self, name="Unknown", repeat=False, shuffle=False):
        self.song_list = []
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.current_song_index = 0
        self.played_songs = set()

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        self.song_list.remove(song)
        try:
            self.song_list.remove(song)
        except ValueError:
            pass

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def get_total_length(self):
        total_seconds = sum(
            [song.get_length(seconds=True) for song in self.song_list])

        hours = total_seconds // 3600
        minutes = (total_seconds - hours * 3600) // 60
        seconds = total_seconds - hours * 3600 - minutes * 60

        if hours == 0:
            return "{}:{}".format(minutes, seconds)
        else:
            return "{}:{}:{}".format(hours, minutes, seconds)

    def get_artists(self):
        artists_histogram = {}

        for song in self.song_list:
            if song.artist in artists_histogram.keys():
                artists_histogram[song.artist] += 1
            else:
                artists_histogram[song.artist] = 1

        return artists_histogram

        # all_artists = [song.artist for song in self.__songs]
        # return {name: all_artists.count(name) for name in all_artists}

    def __has_next_song(self):
        return self.current_song_index < len(self.song_list)

    def shuffle_songs(self):
        song = random.choice(self.song_list)

        while song in self.played_songs:
            song = random.choice(self.song_list)

        self.played_songs.add(song)

        if len(self.song_list) == len(self.played_songs):
            self.played_songs = set()

        return song

    def next_song(self):
        if self.shuffle:
            return self.shuffle_songs()

        elif self.repeat:
            if self.current_song_index == len(self.song_list):
                self.current_song_index = 0
            else:
                song = self.song_list[self.current_song_index]
                self.current_song_index += 1

            return song

        else:
            if self.current_song_index < len(self.song_list):
                song = self.song_list[self.current_song_index]
                self.current_song_index += 1

                return song

            else:
                raise Exception("End of playlist")

    def pprint_playlist(self):
        headers = ["Artist", "Song", "Length"]
        table = []

        for song in self.song_list:
            table.append([song.artist, song.title, song.length])

        return tabulate(table, headers=headers)

    def prepare_json(self):
        data = {
            "name": self.name,
            "songs": [song.prepare_json() for song in self.song_list],
            "repeat": self.repeat,
            "shuffle": self.shuffle
        }

        return data

    def save(self, indent=True):
        filename = "./playlist-data/" + self.name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=4))

    @staticmethod
    def load(filename):
        with open("./playlist-data/" + filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"], data["repeat"], data["shuffle"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"],
                            title=dict_song["title"],
                            album=dict_song["album"],
                            length=dict_song["length"])
                p.add_song(song)

            return p

    def test_load(filename):
        p = Playlist.load(filename)
        try:
            while True:
                song = p.next_song()
                print(str(song))
                time.sleep(1)
        except Exception as e:
            print(e)
