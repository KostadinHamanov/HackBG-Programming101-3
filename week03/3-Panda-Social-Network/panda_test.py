from panda import Panda
import unittest


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")

    def test_init(self):
        self.assertEqual(self.ivo.m_name, "Ivo")
        self.assertEqual(self.ivo.m_email, "ivo@pandamail.com")
        self.assertEqual(self.ivo.m_gender, "male")
        self.assertTrue(isinstance(self.ivo, Panda))

    def test_get_name(self):
        self.assertEqual(self.ivo.get_name(), self.ivo.m_name)

    def test_get_email(self):
        self.assertEqual(self.ivo.get_email(), self.ivo.m_email)

    def test_get_gender(self):
        self.assertEqual(self.ivo.get_gender(), self.ivo.m_gender)

    def test_isMale(self):
        self.assertTrue(self.ivo.isMale())
        self.assertTrue(self.rado.isMale())

    def test_isFemale(self):
        self.assertFalse(self.ivo.isFemale())
        self.assertFalse(self.rado.isFemale())

    def test_data_equality(self):
        self.assertFalse(self.ivo == self.rado)
        self.assertFalse(self.rado == self.tony)
        self.assertTrue(self.rado == self.rado)

    def test_convertion_panda_to_string(self):
        self.assertTrue(str(self.ivo) == "Ivo - ivo@pandamail.com - male")
        self.assertTrue(str(self.rado) == "Rado - rado@pandamail.com - male")

    def test_hashing(self):
        self.assertTrue(type(hash(str(self.ivo) == int)))

    def test_email_validity(self):
        ivan = Panda("Ivan", "ivan@panda@mail.com", "male")
        self.assertTrue(self.ivo.is_email_valid(self.ivo.m_email))
        self.assertFalse(ivan.is_email_valid(ivan.m_email))

if __name__ == '__main__':
    unittest.main()
