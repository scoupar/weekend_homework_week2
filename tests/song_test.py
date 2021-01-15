import unittest

from src.song import Song

class TestSong (unittest.TestCase):

    def setUp(self):
        self.song = Song("Justboy", "Biffy Clyro")
    


    def test_song_has_title(self):
        self.assertEqual("Justboy", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Biffy Clyro", self.song.artist)

