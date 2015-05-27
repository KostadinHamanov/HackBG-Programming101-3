import unittest
from hall import Hall


class HallTest(unittest.TestCase):

    def setUp(self):
        self.hall = Hall()

    def test_new_instance(self):
        self.assertTrue(self.hall, Hall)

    def test_valid_members(self):
        places = [
            ['  ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['1 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['2 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['3 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['4 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['5 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['6 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['7 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['8 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['9 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]

        self.assertEqual(self.hall.places, places)

    def test_set_busy_seat(self):
        self.hall.set_busy_seat(5, 5)
        self.assertEqual(self.hall.places[5][5], 'X')

if __name__ == '__main__':
    unittest.main()
