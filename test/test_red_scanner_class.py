
import unittest

from redsugar.scanner import RedScanner
from redsugar.sourcer import RedSourcer

TESTING_SOURCE_CODE = """fn hello do
    print "hello world"
end
"""


class TestRedScanner(unittest.TestCase):
    """
    TestRedScanner is moves through the source a character at a time
    and is used by the lexer to tranverse the redsugar source code.
    """
    def setUp(self):
        self.sourcer = RedSourcer('test/sample_source_1.reds')
        self.scanner = RedScanner(TESTING_SOURCE_CODE)

    def test_text_contains_source(self):
        self.assertEqual(self.scanner.text, TESTING_SOURCE_CODE)

    def tearDown(self):
        pass

    def test_start(self):
        first_char = self.scanner.start()
        self.assertEqual(first_char, 'f')
