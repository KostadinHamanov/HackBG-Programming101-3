from directed_graph import DirectedGraph
from directed_graph import NodeAlreadyInGraph
from directed_graph import CannotFollowYourself
import unittest


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.connection = DirectedGraph()

    def test_init(self):
        self.assertTrue(isinstance(self.connection, DirectedGraph))

    def test_add_node(self):
        self.connection.add_node('Person')
        self.assertTrue('Person' in self.connection.graph)
        with self.assertRaises(NodeAlreadyInGraph):
            self.connection.add_node('Person')

    def test_add_edge(self):
        pesho = "Pesho"
        gosho = "Gosho"
        self.connection.add_edge(pesho, gosho)
        self.assertTrue(gosho in self.connection.graph[pesho])
        self.assertTrue(pesho not in self.connection.graph[gosho])
        with self.assertRaises(CannotFollowYourself):
            self.connection.add_edge(gosho, gosho)

    def test_get_neighbours_for(self):
        self.connection.add_edge("Pesho", "Gosho")
        self.connection.add_edge("Gosho", "Rado")
        self.connection.add_edge("Gosho", "Ivo")
        self.assertEqual(self.connection.get_neighbours_for("Pesho"),
                         set(["Gosho"]))
        self.assertEqual(self.connection.get_neighbours_for("Gosho"),
                         set(["Ivo", "Rado"]))
        self.assertEqual(self.connection.get_neighbours_for("Ivo"), set([]))

    def test_bulid_network(self):
        self.connection.add_edge('Pesho', 'Gosho')
        self.connection.add_edge('Gosho', 'Rado')
        self.connection.add_edge('Gosho', 'Ivo')
        self.connection.add_edge('Ivo', 'Ivan')
        self.connection.add_node('Peter')

        self.assertEqual(self.connection.bulid_network('Pesho'),
                         set(["Pesho", "Gosho", "Rado", "Ivo", "Ivan"]))
        self.assertEqual(self.connection.bulid_network('Gosho'),
                         set(["Gosho", "Rado", "Ivo", "Ivan"]))
        self.assertEqual(self.connection.bulid_network('Rado'),
                         set(["Rado"]))
        self.assertEqual(self.connection.bulid_network('Ivo'),
                         set(["Ivo", "Ivan"]))
        self.assertEqual(self.connection.bulid_network('Ivan'),
                         set(["Ivan"]))
        self.assertEqual(self.connection.bulid_network('Peter'),
                         set(["Peter"]))

    def test_edge_between(self):
        self.connection.add_edge('Pesho', 'Gosho')
        self.connection.add_edge('Gosho', 'Rado')
        self.connection.add_edge('Gosho', 'Ivo')

        self.assertTrue(self.connection.edge_between("Pesho", "Gosho"))
        self.assertTrue(self.connection.edge_between("Gosho", "Rado"))
        self.assertTrue(self.connection.edge_between("Gosho", "Ivo"))
        self.assertFalse(self.connection.edge_between("Gosho", "Pesho"))

    def test_path_between(self):
        self.connection.add_edge('Pesho', 'Gosho')
        self.connection.add_edge('Gosho', 'Rado')
        self.connection.add_edge('Gosho', 'Ivo')

        self.assertTrue(self.connection.path_between("Pesho", "Gosho"))
        self.assertTrue(self.connection.path_between("Pesho", "Rado"))
        self.assertTrue(self.connection.path_between("Pesho", "Ivo"))
        self.assertFalse(self.connection.path_between("Ivo", "Pesho"))


if __name__ == '__main__':
    unittest.main()
