import unittest
from hero import Hero
from weapon import Weapon
from spell import Spell


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hunter = Hero("Lagerta", "Arrow", 120, 120, 2)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.hunter, Hero))

    def test_valid_members(self):
        self.assertEqual(self.hunter.name, "Lagerta")
        self.assertEqual(self.hunter.title, "Arrow")
        self.assertEqual(self.hunter.health, 120)
        self.assertEqual(self.hunter.mana, 120)
        self.assertEqual(self.hunter.mana_regeneration_rate, 2)

        self.assertEqual(self.hunter.max_health, 120)
        self.assertEqual(self.hunter.max_mana, 120)

    def test_known_as(self):
        self.assertEqual(self.hunter.known_as(), "Lagerta the Arrow")

    def test_get_health(self):
        self.assertEqual(self.hunter.get_health(), 120)

    def test_get_mana(self):
        self.assertEqual(self.hunter.get_mana(), 120)

    def test_is_alive(self):
        self.assertTrue(self.hunter.is_alive())
        self.hunter.health = 0
        self.assertFalse(self.hunter.is_alive())

    def test_can_cast_without_spell(self):
        self.assertFalse(self.hunter.can_cast())

    def test_can_cast_with_more_mana(self):
        self.hunter.spell = Spell("Chilling Poison", 20, 20, 2)
        self.assertTrue(self.hunter.can_cast())

    def test_can_cast_with_less_mana(self):
        self.hunter.spell = Spell("Chilling Poison", 20, 20, 2)
        self.hunter.mana = 0
        self.assertFalse(self.hunter.can_cast())

    def test_take_damage_more_than_health(self):
        self.hunter.take_damage(150)
        self.assertEqual(self.hunter.health, 0)

    def test_take_damage_less_than_health(self):
        self.hunter.take_damage(100)
        self.assertEqual(self.hunter.health, 20)

    def test_take_healing_dead_hero(self):
        self.hunter.health = 0
        self.assertFalse(self.hunter.take_healing(200))

    def test_take_healing_with_more_points_than_max_health(self):
        self.hunter.health = 80
        self.assertTrue(self.hunter.take_healing(200))
        self.assertEqual(self.hunter.health, 120)

    def test_take_healing_with_less_points_than_max_health(self):
        self.hunter.health = 90
        self.assertTrue(self.hunter.take_healing(20))
        self.assertEqual(self.hunter.health, 110)

    def test_take_mana_with_more_points_than_max_mana(self):
        self.hunter.mana = 80
        self.hunter.take_mana(200)
        self.assertEqual(self.hunter.mana, 120)

    def test_take_mana_with_negative_mana(self):
        self.hunter.mana = 50
        self.hunter.take_mana(-60)
        self.assertEqual(self.hunter.mana, 0)

    def test_take_mana_with_less_points_than_max_mana(self):
        self.hunter.mana = 65
        self.hunter.take_mana(20)
        self.assertEqual(self.hunter.mana, 85)

    def test_equip(self):
        knife = Weapon("Knife", 10)
        self.hunter.equip(knife)
        self.assertEqual(self.hunter.weapon, knife)

    def test_learn(self):
        mind_blast = Spell("Mind Blast", 20, 35, 5)
        self.hunter.learn(mind_blast)
        self.assertEqual(self.hunter.spell, mind_blast)

    def test_attack_without_equiped_weapon(self):
        self.assertEqual(self.hunter.attack(by="weapon"), 0)

    def test_attack_with_equiped_weapon(self):
        knife = Weapon("Sword", 30)
        self.hunter.equip(knife)
        self.assertEqual(self.hunter.attack(by="weapon"), 30)

    def test_attack_without_learned_spell(self):
        self.assertEqual(self.hunter.attack(by="spell"), 0)

    def test_attack_with_learned_spell(self):
        fire_blast = Spell("Fire Blast", 60, 40, 2)
        self.hunter.learn(fire_blast)
        self.assertEqual(self.hunter.attack(by="spell"), 60)

if __name__ == '__main__':
    unittest.main()
