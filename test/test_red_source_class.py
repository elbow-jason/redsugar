import unittest
import redsugar

from redsugar.utils import RedSource


def test_what_is_red_sugar_made_of():
    assert redsugar is not None
    assert redsugar.utils is not None
    assert redsugar.utils.RedSource is not None


class TestRedSource(unittest.TestCase):

    def setUp(self):
        self.source = RedSource('test/sample_source_1.reds')

    def tearDown(self):
        pass

    def test_redsource_initialization(self):
        self.source = RedSource('test/sample_source_1.reds')

    def test_redsource_opens_a_file(self):
        self.source.text = ''
        self.source.text = self.source.read('test/sample_source_1.reds')
        self.assertIn('Jason', self.source.text)
