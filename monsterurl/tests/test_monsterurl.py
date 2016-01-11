import unittest

from monsterurl import get_monster

class TestGetName(unittest.TestCase):
    
    def test_returns_string(self):
        monster = get_monster()
        self.assertIsInstance(monster, str)
        self.assertNotEqual(len(monster), 0)

