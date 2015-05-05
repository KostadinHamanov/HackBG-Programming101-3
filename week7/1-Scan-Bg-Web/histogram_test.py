from histogram import Histogram
import unittest


class TestNetwork(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.h, Histogram))

    def test_count(self):
        self.h.add("Apache")
        self.h.add("Apache")
        self.h.add("nginx")
        self.h.add("IIS")
        self.h.add("nginx")

        self.assertEqual(self.h.count("Apache"), 2)
        self.assertEqual(self.h.count("nginx"), 2)
        self.assertEqual(self.h.count("IIS"), 1)

        self.assertTrue(self.h.count("Apache") == 2)
        self.assertTrue(self.h.count("nginx") == 2)
        self.assertTrue(self.h.count("IIS") == 1)
        self.assertTrue(self.h.count("IBM Web Server") is None)

    def test_get_dict(self):
        self.h.add("Apache")
        self.h.add("Apache")
        self.h.add("nginx")
        self.h.add("IIS")
        self.h.add("nginx")
        expected_result = {"Apache": 2, "IIS": 1, "nginx": 2}
        self.assertEqual(self.h.get_dict(), expected_result)

if __name__ == '__main__':
    unittest.main()
