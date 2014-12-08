import unittest


class SanityTester(unittest.TestCase):
    def setUp(self):
        self.name = "sanity tester"
        self.true = True
        self.false = False

    def tearDown(self):
        print "tear it down!!!"

    def test_true(self):
        self.assertEqual(True, self.true)

    def test_false(self):
        self.assertEqual(False, self.false)

    def test_name(self):
        self.assertEqual('sanity tester', self.name)
