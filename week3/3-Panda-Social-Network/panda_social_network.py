from panda import Panda
import json


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.network = {}

    def has_panda(self, panda):
        if panda in self.network:
            return True
        return False

    def __getitem__(self, index):
        return self.network[index]

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThere

        self.network[panda] = []

    def are_friends(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False

        if panda1 in self.network[panda2] and panda2 in self.network[panda1]:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def friends_of(self, panda):
        if panda not in self.network.keys():
            return False
        return self.network[panda]

    def connection_level(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            return 1
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False
        if self.bfs(panda1, panda2) == 0:
            return -1
        else:
            return self.bfs(panda1, panda2)

    def bfs(self, panda1, panda2):
        visited = set()
        queue = []
        path_to = {}

        queue.append(panda1)
        visited.add(panda1)
        path_to[panda1] = None
        found = False
        path_length = 0

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == panda2:
                found = True
                break
            for neighbour in self.network[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)

        if found:
            while path_to[panda2] is not None:
                path_length += 1
                panda2 = path_to[panda2]

        return path_length

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        else:
            return False

    def how_many_gender_in_network(self, level, panda, gender):
        gender_count = 0

        for friend in self.network:
            current_level = self.connection_level(panda, friend)
            if friend != panda and current_level <= level and \
                    friend.get_gender() == gender and current_level != -1:
                gender_count += 1

        return gender_count

    def save(self, path):
        pandas_data = {}
        for panda in self.network:
            pandas_data[repr(panda)] = []
            for friend in self.network[panda]:
                pandas_data[repr(panda)] += [repr(friend)]

        json_string = json.dumps(pandas_data, indent=4)
        with open(path, "w") as save_file:
            save_file.write(json_string)

    def load(self, path):
        contents = {}
        with open(path, "r") as load_file:
            contents = json.loads(load_file.read())

        for panda in contents.keys():
            for friend in contents[panda]:
                if not self.are_friends(panda, friend):
                    self.make_friends(panda, friend)

        return self


def main():
    ivo = Panda("ivo", "ivo@gmail.com", "male")
    rado = Panda("rado", "radorado@mail.bg", "male")
    mary = Panda("mary", "mary@abv.bg", "female")
    tony = Panda("tony", "tony@mail.bg", "female")
    network = PandaSocialNetwork()
    network.add_panda(ivo)
    network.add_panda(rado)
    network.add_panda(mary)
    network.make_friends(ivo, rado)
    network.make_friends(rado, mary)
    network.make_friends(ivo, tony)
    network.save("panda_social_network.json")

    new_network = PandaSocialNetwork()
    new_network.load("panda_social_network.json")
    print (new_network.network)

if __name__ == '__main__':
    main()
