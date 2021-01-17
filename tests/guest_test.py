import unittest

from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 10)
        self.room = Room("Room 1", 2, 5)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(10, self.guest.wallet)

    def test_guest_can_pay_entry_fee(self):
        self.guest.pay_fee(self.room)
        self.assertEqual(5, self.guest.wallet)