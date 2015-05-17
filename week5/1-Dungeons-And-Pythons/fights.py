from random import randint
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class Fight:

    @staticmethod
    def make_enemy():
        random_health = randint(0, 100)
        random_mana = randint(0, 100)
        random_damage = randint(0, 20)

        enemy = Enemy(random_health, random_mana, random_damage)
        enemy.equip(Weapon("Bow", 10))
        enemy.learn(Spell("Golden Arrow", 10, 10, 2))

        return enemy

    @staticmethod
    def attack_by_spell(attacked, attacking, type_attack, type_defend, tool):
        result = ''
        attacked.take_damage(attacking.attack(by='spell'))
        result = '{} casts a {}'.format(type_attack, tool.get_name())
        result += ', hits {} for '.format(type_defend)
        result += str(attacking.attack(by='spell'))
        result += '. {} health is '.format(type_defend)
        result += str(attacking.get_health())

        return result

    @staticmethod
    def attack_by_weapon(attacked,  attacking, type_attack, type_defend, tool):
        result = ''
        attacked.take_damage(attacking.attack(by='weapon'))
        result = '{} hits with {}'.format(type_attack, tool.get_name())
        result += ' for ' + str(attacking.attack(by='weapon'))
        result += '. {} health is '.format(type_defend)
        result += str(attacked.get_health())

        return result

    @staticmethod
    def spell_or_weapon(hero):
        if hero.can_cast() and hero.spell.get_damage() >\
                hero.weapon.get_damage():
            return hero.spell
        else:
            return hero.weapon

    @staticmethod
    def move_enemy(hero_y, hero_x, enemy_y, enemy_x):
        if enemy_x > hero_x:
            enemy_x -= 1
        elif enemy_x < hero_x:
            enemy_x += 1
        elif enemy_y > hero_y:
            enemy_y -= 1
        elif enemy_y < hero_y:
            enemy_y += 1
        print('Enemy is moving!')
        return [enemy_y, enemy_x]

    @staticmethod
    def attack_enemy(hero, enemy, on_same_field, hero_y, hero_x,
                     enemy_y, enemy_x, level_map):

        isFightingOn = hero.is_alive() and enemy.is_alive()
        level_map[enemy_x][enemy_y] = '.'
        while isFightingOn:

            fighting_tool = Fight.spell_or_weapon(hero)
            if not on_same_field:
                print(
                    Fight.attack_by_spell(
                        enemy, hero, 'Hero', 'Enemy', hero.spell))
            else:
                if isinstance(fighting_tool, Spell):
                    hero.spell = fighting_tool
                    print(
                        Fight.attack_by_spell(
                            enemy, hero, 'Hero', 'Enemy', hero.spell))
                else:
                    print(
                        Fight.attack_by_weapon(
                            enemy, hero, 'Hero', 'Enemy', hero.weapon))

            isFightingOn = hero.is_alive() and enemy.is_alive()
            if not isFightingOn:
                break

            if on_same_field:
                fighting_tool = Fight.spell_or_weapon(enemy)
                if isinstance(fighting_tool, Spell):
                    print(
                        Fight.attack_by_spell(
                            hero, enemy, 'Enemy', 'Hero', enemy.spell))
                else:
                    print(Fight.attack_by_weapon(
                        hero, enemy, 'Enemy', 'Hero', enemy.weapon))
            else:
                enemy_cords = Fight.move_enemy(
                    hero_y, hero_x, enemy_y, enemy_x, level_map, 'E', '.')
                enemy_y = enemy_cords[0]
                enemy_x = enemy_cords[1]

            isFightingOn = hero.is_alive() and enemy.is_alive()
            if not isFightingOn:
                break

        if enemy.is_alive():
            level_map[hero_y][hero_x] = 'E'
