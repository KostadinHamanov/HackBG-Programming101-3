class NodeAlreadyInGraph(Exception):
    pass


class CannotFollowYourself(Exception):
    pass


class DirectedGraph():

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node in self.graph:
            raise NodeAlreadyInGraph
        self.graph[node] = set()

    def get_info(self):
        return self.graph

    # def has_node(self, node):
    #     if node in self.graph:
    #         return True
    #     return False

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph:
            self.add_node(node_a)

        if node_b not in self.graph:
            self.add_node(node_b)

        if node_a == node_b:
            raise CannotFollowYourself

        self.graph[node_a].add(node_b)

    def get_neighbours_for(self, current_node):
        return self.graph[current_node]

    def bulid_network(self, start):
        visited = set()
        queue = []

        visited.add(start)
        queue.append(start)

        while len(queue) != 0:
            current_node = queue.pop(0)

            network = self.get_neighbours_for(current_node)

            for follower in network:
                if follower not in visited:
                    queue.append(follower)
                    visited.add(follower)

        return visited

    def edge_between(self, node_a, node_b):
        print ("node_b:")
        print (node_b)
        print ("self.graph[node_a]")
        print (self.graph[node_a])
        if node_b in self.graph[node_a]:
            return True
        return False

    def path_between(self, node_a, node_b):
        visited = set()
        queue = []

        visited.add(node_a)
        queue.append(node_a)

        while len(queue) != 0:
            current_node = queue.pop(0)
            for node in self.graph[current_node]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)

        all_visited = visited
        if node_b in all_visited:
            return True
        return False
