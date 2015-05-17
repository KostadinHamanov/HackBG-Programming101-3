import unittest
from dungeon import Dungeon
from hero import Hero
from spell import Spell
from weapon import Weapon


class DungeonTest(unittest.TestCase):

    def setUp(self):
        self.new_map = [
            ['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
            ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
            ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
            ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
            ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']
        ]
        self.dungeon = Dungeon(self.new_map)
        self.hero = Hero("Floki", "Builder", 100, 100, 2)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.dungeon, Dungeon))

    def test_valid_members(self):
        self.assertEqual(self.dungeon.map, self.new_map)
        self.assertEqual(self.dungeon.spawning_points, [(0, 0)])
        self.assertEqual(self.dungeon.hero, None)
        self.assertEqual(self.dungeon.hero_x, None)
        self.assertEqual(self.dungeon.hero_y, None)

    def test_spawn(self):
        self.assertTrue(self.dungeon.spawn(self.hero))
        self.assertEqual(self.dungeon.hero.health, 100)
        self.assertEqual(self.dungeon.hero.mana, 100)
        self.assertEqual(self.dungeon.hero_x, 0)
        self.assertEqual(self.dungeon.hero_y, 0)

    def test_move(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.move_hero("u"))
        self.assertIsNone(self.dungeon.move_hero("r"))
        self.assertIsNone(self.dungeon.move_hero("d"))
        self.assertEqual(self.dungeon.hero_x, 1)
        self.assertEqual(self.dungeon.hero_y, 1)
        self.assertIsNone(self.dungeon.move_hero("d"))
        self.assertEqual(self.dungeon.hero_x, 2)
        self.assertEqual(self.dungeon.hero_y, 1)

if __name__ == '__main__':
    unittest.main()
