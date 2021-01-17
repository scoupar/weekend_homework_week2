import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", 2, 5)
        self.guest = Guest("John", 10)
        self.guest2 = Guest("Dave", 3)
        self.guest3 = Guest("Amy", 5)
        self.song = Song("Justboy", "Biffy Clyro")

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def test_guest_list_starts_at_0(self):
        self.assertEqual(0, len(self.room.guest_list))

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guest_list))

    def test_can_remove_guest_from_room(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guest_list))

    def test_can_add_song_to_room(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.play_list))
    
    def test_room_cant_be_overbooked(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        self.assertEqual(2, len(self.room.guest_list))

    def test_guest_pay_fee_adds_to_till(self):
        self.guest.pay_fee(self.room)
        self.assertEqual(5, self.room.till)
        
