import unittest
from spell import Spell


class SpellTest(unittest.TestCase):

    def setUp(self):
        self.spell = Spell("Froze", 20, 10, 3)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.spell, Spell))

    def test_valid_members(self):
        self.assertEqual(self.spell.name, "Froze")
        self.assertEqual(self.spell.damage, 20)
        self.assertEqual(self.spell.mana_cost, 10)
        self.assertEqual(self.spell.cast_range, 3)

    def test_str(self):
        name = self.spell.name
        damage = self.spell.damage
        mana_cost = self.spell.mana_cost
        cast_range = self.spell.cast_range

        expected = "{} with damage: {}, mana_cost: {}, cast_range: {}"
        expected = expected.format(name, damage, mana_cost, cast_range)
        self.assertEqual(str(self.spell), expected)

    def test_get_functions(self):
        self.assertEqual(self.spell.get_name(), "Froze")
        self.assertEqual(self.spell.get_damage(), 20)
        self.assertEqual(self.spell.get_mana_cost(), 10)
        self.assertEqual(self.spell.get_cast_range(), 3)

    def test_prepare_json(self):
        data = {
            "name": "Froze",
            "damage": 20,
            "mana_cost": 10,
            "cast_range": 3
        }
        self.assertEqual(self.spell.prepare_json(), data)

if __name__ == '__main__':
    unittest.main()
