import unittest

from redsugar.sourcer import RedSourcer

TESTING_FILE_PATH = 'test/sample_source_1.reds'


class TestRedSource(unittest.TestCase):

    def setUp(self):
        self.sourcer = RedSourcer(TESTING_FILE_PATH)

    def tearDown(self):
        pass

    def test_path(self):
        self.assertEqual(self.sourcer.path, TESTING_FILE_PATH)

    def test_redsource_opens_a_file(self):
        self.sourcer.text = ''
        self.sourcer.text = self.sourcer.read(TESTING_FILE_PATH)
        self.assertIn('Jason', self.sourcer.text)
