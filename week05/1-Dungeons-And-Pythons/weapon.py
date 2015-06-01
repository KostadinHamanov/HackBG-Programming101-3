import json
from random import randint


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        message = "{} with damage = {}"
        message = message.format(self.name, self.damage)

        return message

    def get_damage(self):
        return self.damage

    def get_name(self):
        return self.name

    def prepare_json(self):
        data = {
            "name": self.name,
            "damage": self.damage
        }

        return data

    def save(self):
        with open("weapons.json", "w") as text_file:
            text_file.write(json.dumps(self.prepare_json(), 4))

    @staticmethod
    def load(path):
        with open(path) as text_file:
            file_content = text_file.read()

            data = json.loads(file_content)

            name = data[randint(0, len(data) - 1)]["name"]
            damage = data[randint(0, len(data) - 1)]["damage"]

            return Weapon(name, damage)
