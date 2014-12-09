
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

    def test_starts_at_position_0(self):
        self.assertEqual(self.scanner.position, 0)

    def test_next(self):
        self.scanner.position = 1
        self.scanner.next()
        self.assertEqual(self.scanner.position, 2)

    def test_prev(self):
        self.scanner.position = 2
        self.scanner.prev()
        self.assertEqual(self.scanner.position, 1)

    def test_get(self):
        self.scanner.position = 1
        current_char = self.scanner.get()
        self.assertEqual(current_char, 'n')

    def test_mark(self):
        self.scanner.position = 2
        self.scanner.mark()
        self.assertEqual(self.scanner.marker, 2)

    def test_diff(self):
        self.scanner.marker = 6
        self.scanner.position = 2
        delta = self.diff()
        self.assertEqual(delta, -4)
        self.scanner.position = 12
        delta = self.diff()
        self.assertEqual(delta, 6)

    def test_goto(self):
        self.scanner.goto(3)
        self.assertEqual(self.scanner.position, 3)

    def test_find_next(self):
        self.scanner.text = """Jason Louis"""
        self.scanner.position = 3
        should_be_o = self.scanner.get()
        should_be_7 = self.scanner.find_next('o')
        self.assertEqual(should_be_o, 'o')
        self.assertEqual(should_be_7, 7)
