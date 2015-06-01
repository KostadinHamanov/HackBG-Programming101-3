from panda import Panda
from panda_social_network import PandaSocialNetwork
from panda_social_network import PandaAlreadyThere
from panda_social_network import PandasAlreadyFriends
import unittest


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")
        self.pesho = Panda("Pesho", "pesho@pandamail.com", "male")
        self.maria = Panda("Maria", "maria@pandamail.com", "female")
        self.vera = Panda("Vera", "vera@pandamail.com", "female")

    def test_init(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_adding_panda(self):
        self.network.add_panda(self.tony)
        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.tony)

    def test_has_panda(self):
        self.network.add_panda(self.tony)
        self.assertTrue(self.network.has_panda(self.tony))

    def test_make_friends_who_are_in_network(self):
        self.network.add_panda(self.rado)
        self.network.add_panda(self.ivo)
        self.network.make_friends(self.rado, self.ivo)
        with self.assertRaises(PandasAlreadyFriends):
            self.network.make_friends(self.rado, self.ivo)

    def test_make_friends_who_are_not_in_network(self):
        self.network.make_friends(self.rado, self.tony)
        self.assertTrue(self.network.has_panda(self.rado))
        self.assertTrue(self.network.has_panda(self.tony))

    def test_are_friends(self):
        self.network.make_friends(self.rado, self.ivo)
        self.assertTrue(self.network.are_friends(self.ivo, self.rado))
        self.assertFalse(self.network.are_friends(self.ivo, self.tony))

    def test_friends_of(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertEqual(self.network.friends_of(self.ivo), [self.rado])
        self.assertFalse(self.network.friends_of(self.tony))

    def test_connection_level_if_pandas_are_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.connection_level
                        (self.ivo, self.rado) == 1)

    def test_connection_level_if_pandas_are_not_member_of_the_network(self):
        self.network.add_panda(self.maria)
        self.assertFalse(self.network.connection_level(self.maria, self.rado))
        self.assertFalse(self.network.connection_level(self.rado, self.ivo))

    def test_connection_level(self):
        self.network.make_friends(self.rado, self.ivo)
        self.network.make_friends(self.ivo, self.tony)
        self.network.make_friends(self.tony, self.maria)
        self.network.make_friends(self.rado, self.vera)
        self.network.add_panda(self.pesho)

        self.assertTrue(self.network.
                        connection_level(self.ivo, self.rado) == 1)
        self.assertTrue(self.network.
                        connection_level(self.ivo, self.tony) == 1)
        self.assertTrue(self.network.
                        connection_level(self.ivo, self.maria) == 2)
        self.assertTrue(self.network.
                        connection_level(self.rado, self.tony) == 2)
        self.assertTrue(self.network.
                        connection_level(self.rado, self.maria) == 3)
        self.assertTrue(self.network.
                        connection_level(self.vera, self.ivo) == 2)
        self.assertTrue(self.network.
                        connection_level(self.vera, self.maria) == 4)
        self.assertTrue(self.network.
                        connection_level(self.pesho, self.rado) == -1)

    def test_are_connected(self):
        self.network.make_friends(self.rado, self.ivo)
        self.network.make_friends(self.ivo, self.tony)
        self.network.make_friends(self.tony, self.maria)
        self.network.make_friends(self.rado, self.vera)
        self.network.add_panda(self.pesho)

        self.assertTrue(self.network.are_connected(self.rado, self.maria))
        self.assertFalse(self.network.are_connected(self.vera, self.pesho))

    def test_how_many_gender_in_network(self):
        self.network.make_friends(self.rado, self.ivo)
        self.network.make_friends(self.ivo, self.tony)
        self.network.make_friends(self.tony, self.maria)
        self.network.make_friends(self.rado, self.vera)
        self.network.add_panda(self.pesho)

        self.assertEqual(self.network.how_many_gender_in_network
                         (1, self.ivo, "female"), 1)
        self.assertEqual(self.network.how_many_gender_in_network
                         (2, self.tony, "male"), 2)
        self.assertEqual(self.network.how_many_gender_in_network
                         (2, self.maria, "male"), 1)


if __name__ == '__main__':
    unittest.main()
