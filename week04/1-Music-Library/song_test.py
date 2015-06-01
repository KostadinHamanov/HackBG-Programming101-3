from song import Song
import unittest


class TestSong(unittest.TestCase):

    def setUp(self):
        self.odin = Song(title="Odin", artist="Manowar",
                         album="The Sons of Odin", length="3:44")
        self.runaway = Song(title="Runaway", artist="Bon Jovi",
                            album="Greatest Hits - The Ultimate", length="3:51")

    def test_init(self):
        self.assertTrue(isinstance(self.odin, Song))

    def test_equality(self):
        self.assertFalse(self.odin == self.runaway)
        self.assertTrue(self.odin == self.odin)

    def test_hash(self):
        self.assertIsNotNone(hash(self.odin))
        self.assertTrue(isinstance(hash(self.runaway), int))

    def test_get_hours(self):
        self.assertEqual(self.runaway.get_hours(), 0)

    def test_get_seconds(self):
        self.assertEqual(self.runaway.get_seconds(), 231)

    def test_get_minutes(self):
        self.assertEqual(self.runaway.get_minutes(), 3)

    def test_get_length(self):
        self.assertEqual(self.odin.get_length(), "3:44")

    # def test_length_not_proper_format(self):
    #     odin = Song(title="Odin", artist="Manowar",
    #                 album="The Sons of Odin", length="3:44:12:3")

    #     with self.assertRaises(ValueError):
    #         odin.get_length()

    def test_prepare_json(self):
        expected = {'artist': 'Manowar', 'title': 'Odin', 'hours': 0,
                    'length': '3:44', 'seconds': 44, 'minutes': 3,
                    'album': 'The Sons of Odin', 'path': ''}

        self.assertEqual(self.odin.prepare_json(), expected)


if __name__ == '__main__':
    unittest.main()
