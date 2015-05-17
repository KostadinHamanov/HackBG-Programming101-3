from treasure import Treasure
from fights import Fight


class Dungeon:

    SPAWN_PLACE = "S"
    GATEWAY_PLACE = "G"
    OBSTACLE_PLACE = "#"
    PATH_PLACE = "."
    TREASURE_PLACE = "T"
    ENEMY_PLACE = "E"
    HERO_PLACE = "H"

    @staticmethod
    def load_map_from_file(path):
        with open(path, "r") as file_text:
            content = file_text.read().splitlines()
            new_dungeon_map = [list(line) for line in content]

        return Dungeon(new_dungeon_map)

    def print_map(self):
        for line in self.map:
            print("".join(line))

    def get_map(self):
        return self.map

    def get_spawning_points(self):
        return self.spawning_points

    def get_hero(self):
        return self.hero

    def get_hero_x(self):
        return self.hero_x

    def get_hero_y(self):
        return self.hero_y

    def __init__(self, dungeon_map):
        self.map = dungeon_map
        self.spawning_points = self.find_spawn_points()
        self.hero = None
        self.hero_x = None
        self.hero_y = None

    def find_spawn_points(self):
        points = []
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] == Dungeon.SPAWN_PLACE:
                    points.append((i, j))

        return points

    def spawn(self, hero):
        if self.spawning_points != []:
            self.hero = hero
            self.hero_x, self.hero_y = self.spawning_points[0]
            self.map[self.hero_x][self.hero_y] = Dungeon.HERO_PLACE
            self.spawning_points = self.spawning_points[1:]
            return True
        else:
            return False

    def move_hero(self, direction):
        new_x = 0
        new_y = 0

        if direction == "r":
            new_x = self.hero_x
            new_y = self.hero_y + 1

        if direction == "l":
            new_x = self.hero_x
            new_y = self.hero_y - 1

        if direction == "u":
            new_x = self.hero_x - 1
            new_y = self.hero_y

        if direction == "d":
            new_x = self.hero_x + 1
            new_y = self.hero_y

        if not self.is_inside_the_borders_or_obstacle(new_x, new_y):
            return False

        self.hero.take_mana(self.hero.mana_regeneration_rate)

        self.map[self.hero_x][self.hero_y] = Dungeon.PATH_PLACE
        new_position = self.map[new_x][new_y]
        self.hero_x = new_x
        self.hero_y = new_y

        if new_position == Dungeon.SPAWN_PLACE:
            self.map[self.hero_x][self.hero_y] = Dungeon.HERO_PLACE

        if new_position == Dungeon.PATH_PLACE:
            self.map[self.hero_x][self.hero_y] = Dungeon.HERO_PLACE

        if new_position == Dungeon.GATEWAY_PLACE:
            self.map[self.hero_x][self.hero_y] = Dungeon.HERO_PLACE
            return True

        if new_position == Dungeon.TREASURE_PLACE:
            Treasure.get_random_treasure(self.hero)
            self.map[self.hero_x][self.hero_y] = Dungeon.HERO_PLACE

        if new_position == Dungeon.ENEMY_PLACE:
            self.hero_attack(self.hero)
            return False

    def is_inside_the_borders_or_obstacle(self, x, y):

        if x < 0 or x >= len(self.map):
            return False

        if y < 0 or y >= len(self.map[0]):
            return False

        if self.map[x][y] == Dungeon.OBSTACLE_PLACE:
            return False

        return True

    def hero_attack(self, hero):
        casting_range = 0

        enemy_position = self.check_enemy_in_range(casting_range)
        is_enemy = enemy_position is not None

        if not is_enemy and not self.hero.can_cast():
            print("Can not cast magic.")
            return 0

        if self.hero.spell is not None:
            casting_range = self.hero.spell.get_cast_range()
        else:
            casting_range = 0

        position = self.check_enemy_in_range(casting_range)
        is_enemy = position is not None

        if not is_enemy:
            print("Nothing in range" + str(self.hero.spell.get_cast_range()))
            return 0

        enemy_x = position[0]
        enemy_y = position[1]
        enemy = Fight.make_enemy()
        Fight.attack_enemy(self.hero, enemy, is_enemy,
                           self.hero_x, self.hero_y,
                           enemy_y, enemy_x, self.map)

        if not self.hero.is_alive():
            self.map[self.hero_x][self.hero_y] = Dungeon.ENEMY_PLACE
            print('Hero is dead')
            return -1
        else:
            print('Enemy is dead')
            self.map[self.hero_x][self.hero_y] = Dungeon.HERO_PLACE
            return 1

    def check_enemy_in_range(self, cast_range):
        range_list = list(range(0, cast_range + 1))

        x = self.hero_x
        y = self.hero_y

        height = len(self.map)
        width = len(self.map[0])

        for cast_range in range_list:
            out_of_dungeon_left_end = x - cast_range < 0
            out_of_dungeon_right_end = x + cast_range >= height
            out_of_dungeon_up_end = y - cast_range < 0
            out_of_dungeon_down_end = y + cast_range >= width

            if not out_of_dungeon_left_end:
                x_coord = self.hero_x - cast_range
                y_coord = self.hero_y
                if self.map[x_coord][y_coord] == Dungeon.OBSTACLE_PLACE:
                    out_of_dungeon_left_end = True
                if self.map[x_coord][y_coord] == Dungeon.ENEMY_PLACE:
                    return [x_coord, y_coord]

            if not out_of_dungeon_right_end:
                x_coord = self.hero_x + cast_range
                y_coord = self.hero_y
                if self.map[x_coord][y_coord] == Dungeon.OBSTACLE_PLACE:
                    out_of_dungeon_right_end = True
                if self.map[x_coord][y_coord] == Dungeon.ENEMY_PLACE:
                    return [x_coord, y_coord]

            if not out_of_dungeon_up_end:
                x_coord = self.hero_x
                y_coord = self.hero_y - cast_range
                if self.map[x_coord][y_coord] == Dungeon.OBSTACLE_PLACE:
                    out_of_dungeon_up_end = True
                if self.map[x_coord][y_coord] == Dungeon.ENEMY_PLACE:
                    return [x_coord, y_coord]

            if not out_of_dungeon_down_end:
                x_coord = self.hero_x
                y_coord = self.hero_y + cast_range
                if self.map[x_coord][y_coord] == Dungeon.OBSTACLE_PLACE:
                    out_of_dungeon_down_end = True
                if self.map[x_coord][y_coord] == Dungeon.ENEMY_PLACE:
                    return [x_coord, y_coord]
