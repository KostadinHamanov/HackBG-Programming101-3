import json
from random import randint


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        message = "{} with damage: {}, mana_cost: {}, cast_range: {}"

        name = self.name
        damage = self.damage
        mana_cost = self.mana_cost
        cast_range = self.cast_range

        message = message.format(name, damage, mana_cost, cast_range)

        return message

    def get_damage(self):
        return self.damage

    def get_name(self):
        return self.name

    def get_mana_cost(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range

    def prepare_json(self):
        data = {
            "name": self.name,
            "damage": self.damage,
            "mana_cost": self.mana_cost,
            "cast_range": self.cast_range
        }

        return data

    def save(self):
        with open("spells.json", "w") as text_file:
            text_file.write(json.dumps(self.prepare_json(), indent=True))

    @staticmethod
    def load(path):
        with open(path) as text_file:
            file_content = text_file.read()

            data = json.loads(file_content)

            name = data[randint(0, len(data) - 1)]["name"]
            damage = data[randint(0, len(data) - 1)]["damage"]
            mana_cost = data[randint(0, len(data) - 1)]["mana_cost"]
            cast_range = data[randint(0, len(data) - 1)]["cast_range"]

            return Spell(name, damage, mana_cost, cast_range)
