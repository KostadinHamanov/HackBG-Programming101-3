from song import Song
from playlist import Playlist
import unittest


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.test_playlist = Playlist(name="Music", repeat=True, shuffle=True)

        self.odin = Song(title="Odin", artist="Manowar",
                         album="The Sons of Odin", length="3:44")

        self.its_my_life = Song(title="Its my life", artist="Bon Jovi",
                                album="Crush", length="3:46")

        self.back_in_black = Song(title="Back In Black", artist="AC/DC",
                                  album="Back In Back", length="4:02")

    def test_is_instance(self):
        self.assertTrue(isinstance(self.test_playlist, Playlist))

    def test_init(self):
        self.assertEqual(self.test_playlist.name, "Music")
        self.assertEqual(self.test_playlist.repeat, True)
        self.assertEqual(self.test_playlist.shuffle, True)
        self.assertEqual(self.test_playlist.current_song_index, 0)
        self.assertEqual(self.test_playlist.song_list, [])
        self.assertEqual(self.test_playlist.played_songs, set())

    def test_add_song(self):
        self.test_playlist.add_song(self.odin)
        self.assertTrue(self.odin in self.test_playlist.song_list)

    def test_remove_song(self):
        self.test_playlist.add_song(self.odin)
        self.test_playlist.remove_song(self.odin)
        self.assertFalse(self.odin in self.test_playlist.song_list)

    def test_add_songs(self):
        songs = [self.its_my_life, self.back_in_black]
        self.test_playlist.add_songs(songs)
        self.assertTrue(self.its_my_life in self.test_playlist.song_list)
        self.assertTrue(self.back_in_black in self.test_playlist.song_list)

    def test_get_total_length(self):
        self.test_playlist.song_list = [self.its_my_life, self.back_in_black]
        self.assertEqual(self.test_playlist.get_total_length(), "7:48")

    def test_get_artists(self):
        songs = [self.its_my_life, self.back_in_black]
        self.test_playlist.song_list = songs
        arist_histogram = {"AC/DC": 1, "Bon Jovi": 1}
        self.assertEqual(self.test_playlist.get_artists(), arist_histogram)

    def test_shuffle_songs(self):
        songs = [self.its_my_life, self.back_in_black]
        self.test_playlist.song_list = songs

        self.assertTrue(isinstance(self.test_playlist.shuffle_songs(), Song))

    def test_next_song(self):
        playlist = Playlist("Test", repeat=True, shuffle=False)
        songs = [self.odin, self.its_my_life]
        playlist.song_list = songs

        self.assertEqual(playlist.next_song(), self.odin)
        self.assertEqual(playlist.next_song(), self.its_my_life)

    def test_pprint_playlist(self):
        songs = [self.odin, self.its_my_life, self.back_in_black]
        self.test_playlist.add_songs(songs)

        expected = """Artist    Song           Length
--------  -------------  --------
Manowar   Odin           3:44
Bon Jovi  Its my life    3:46
AC/DC     Back In Black  4:02"""

        self.assertEqual(self.test_playlist.pprint_playlist(), expected)

    def test_prepare_json(self):
        songs = [self.odin, self.its_my_life, self.back_in_black]
        self.test_playlist.add_songs(songs)
        song_dicts = [self.odin.__dict__,
                      self.its_my_life.__dict__,
                      self.back_in_black.__dict__]

        expected_result = {
            "name": self.test_playlist.name,
            "songs": song_dicts,
            "shuffle": self.test_playlist.shuffle,
            "repeat": self.test_playlist.repeat
            }

        self.assertEqual(self.test_playlist.prepare_json(), expected_result)


if __name__ == '__main__':
    unittest.main()
