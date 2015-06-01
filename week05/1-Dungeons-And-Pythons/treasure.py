import random
from spell import Spell
from weapon import Weapon


class Treasure:

    @staticmethod
    def get_random_treasure(creature):
        treasure_types = ["health", "mana", "weapon", "spell"]
        random_treasure = random.choice(treasure_types)

        if random_treasure == "health":
            health_treasure = random.randint(-10, creature.max_health)
            creature.take_healing(health_treasure)

            if creature.health == 0:
                message = "Found potion with {} health. Our hero is dead!"
                message = message.format(health_treasure)
                print(message)
            elif creature.health != 0:
                message = "Found potion with {} health. Now health is {}"
                message = message.format(health_treasure, creature.health)
                print(message)

        elif random_treasure == "mana":
            mana_treasure = random.randint(-10, creature.max_mana)
            creature.take_mana(mana_treasure)

            if creature.mana == 0:
                message = "Found potion with {} mana. Our hero have not mana!"
                message = message.format(mana_treasure)
                print(message)
            elif creature.mana != 0:
                message = "Found potion with {} mana. Now mana is {}"
                message = message.format(mana_treasure, creature.mana)
                print(message)

        elif random_treasure == "weapon":
            weapon_treasure = Weapon.load("weapons.json")
            creature.equip(weapon_treasure)
            print("Our hero equipped: {}".format(str(weapon_treasure)))

        elif random_treasure == "spell":
            spell_treasure = Spell.load("spells.json")
            creature.equip(spell_treasure)
            print("Our hero equipped: {}".format(str(spell_treasure)))
