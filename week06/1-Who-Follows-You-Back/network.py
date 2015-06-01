from directed_graph import DirectedGraph


class TooBigLevel(Exception):
    pass


class Network():

    def __init__(self):
        self.graph = DirectedGraph()
        self.person = None

    def build_network_for(self, person, level):
        if level > 4:
            raise TooBigLevel

        self.person = person
        self.build_followers_network(person, level)
        self.build_following_network(person, level)

    def build_followers_network(self, person, level):
        current_level = 0
        visited = set()
        queue = []

        visited.add(person)
        queue.append((current_level, person))

        while len(queue) != 0:
            current_level, current_user = queue.pop(0)
            if current_level == level:
                break

            if len(current_user.get_followers()) == 0:
                current_user.build_followers()
            followers = current_user.get_followers()

            for follower in followers:
                if follower not in visited:
                    visited.add(follower)
                    queue.append((current_level + 1, follower))
                    self.graph.add_edge(follower, current_user)

    def build_following_network(self, person, level):
        current_level = 0
        visited = set()
        queue = []

        queue.append((current_level, person))
        visited.add(person)

        while len(queue) != 0:
            current_level, current_user = queue.pop(0)
            if current_level == level:
                break

            if len(current_user.get_following()) == 0:
                current_user.build_following()
            followings = current_user.get_following()

            for following in followings:
                if following not in visited:
                    queue.append((current_level + 1, following))
                    visited.add(following)
                    self.graph.add_edge(current_user, following)

    def do_you_follow(self, user):
        return self.graph.edge_between(self.person, user)

    def do_you_follow_indirectly(self, user):
        return self.graph.path_between(self.person, user)

    def does_he_she_follows(self, user):
        return self.graph.edge_between(user, self.person)

    def does_he_she_follows_indirectly(self, user):
        return self.graph.edge_between(self.person, user)

    def who_follows_you_back(self):
        followers = self.person.get_followers()
        following = self.person.get_following()
        following_back = []
        for user in followers:
            if user in following:
                following_back.append(user)
        return following_back
