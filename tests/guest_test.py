import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 10)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(10, self.guest.wallet)