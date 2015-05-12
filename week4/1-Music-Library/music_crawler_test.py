import unittest
from music_crawler import MusicCrawler
import pprint


class MusicCrawlerTest(unittest.TestCase):

    def setUp(self):
        path = "/home/kostadin/Music/Music-Library"
        self.crawler = MusicCrawler(path)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.crawler, MusicCrawler))

    def test_generate_playlist(self):

        playlist = self.crawler.generate_playlist()
        pp_playlist = playlist.pprint_playlist()

        expected_list = """Artist    Song                            Length
--------  ------------------------------  --------
Bon Jovi  I'll Sleep When I'm Dead        0:04:41
Bon Jovi  In And Out Of Love              0:04:26
Bon Jovi  Lost Highway                    0:04:13
Bon Jovi  Blood On Blood                  0:06:16
Bon Jovi  This Ain't A Love Song          0:05:05
Bon Jovi  (You Want To) Make A Memory     0:04:37
Bon Jovi  Keep The Faith                  0:05:43
Bon Jovi  The More Things Change          0:03:53
Bon Jovi  These Days                      0:06:27
Bon Jovi  Someday I'll Be Saturday Night  0:04:38
Bon Jovi  When We Were Beautiful          0:05:17
Bon Jovi  This Is Love This Is Life       0:03:25
Bon Jovi  Blaze Of Glory                  0:05:39
Bon Jovi  Runaway                         0:03:51"""

        self.assertEqual(pp_playlist, expected_list)


if __name__ == "__main__":
    unittest.main()
