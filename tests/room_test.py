import unittest

from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", 6)
        self.guest = Guest("John")

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room.capacity)

    def test_guest_list_starts_at_0(self):
        self.assertEqual(0, len(self.room.guest_list))

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guest_list))

    def test_can_remove_guest_from_room(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guest_list))