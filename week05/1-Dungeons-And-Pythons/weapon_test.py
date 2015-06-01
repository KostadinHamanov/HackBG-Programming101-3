import unittest
from weapon import Weapon


class WeaponTest(unittest.TestCase):

    def setUp(self):
        self.weapon = Weapon("Spike", 200)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.weapon, Weapon))

    def test_valid_members(self):
        self.assertEqual(self.weapon.name, "Spike")
        self.assertEqual(self.weapon.damage, 200)

    def test_str(self):
        expected = "{} with damage = {}"
        expected = expected.format(self.weapon.name, self.weapon.damage)
        self.assertEqual(str(self.weapon), expected)

    def test_get_functions(self):
        self.assertEqual(self.weapon.get_name(), "Spike")
        self.assertEqual(self.weapon.get_damage(), 200)

    def test_prepare_json(self):
        data = {
            "name": "Spike",
            "damage": 200
        }
        self.assertEqual(self.weapon.prepare_json(), data)

if __name__ == '__main__':
    unittest.main()
