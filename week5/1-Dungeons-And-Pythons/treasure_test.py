import unittest
from treasure import Treasure
from hero import Hero
from enemy import Enemy


class TreasureTest(unittest.TestCase):

    def setUp(self):
        self.treasure = Treasure()
        self.hero = Hero("Bjarne", "Bow", 100, 100, 2)
        self.enemy = Enemy(100, 100, 50)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.treasure, Treasure))

if __name__ == '__main__':
    unittest.main()
