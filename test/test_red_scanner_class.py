
import unittest

from redsugar.scanner import RedScanner
#from redsugar.sourcer import RedSourcer

from testing_source_code import TESTING_SOURCE_CODE


class TestRedScanner(unittest.TestCase):
    """
    TestRedScanner is moves through the source a character at a time
    and is used by the lexer to tranverse the redsugar source code.
    """
    def setUp(self):
        #self.sourcer = RedSourcer('test/sample_source_1.redsugar')
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
        self.assertEqual(current_char, 'd')

    def test_mark(self):
        self.scanner.position = 2
        self.scanner.mark()
        self.assertEqual(self.scanner.marker, 2)

    def test_diff(self):
        self.scanner.marker     = 6
        self.scanner.position   = 2
        delta1                  = self.scanner.diff()
        self.scanner.position   = 12
        delta2                  = self.scanner.diff()
        self.assertEqual(delta1, -4)
        self.assertEqual(delta2, 6)

    def test_goto(self):
        self.scanner.goto(3)
        self.assertEqual(self.scanner.position, 3)

    def test_find_next(self):
        self.scanner.text       = """Jason Louis"""
        self.scanner.position   = 3
        should_be_o             = self.scanner.get()
        should_be_7             = self.scanner.find_next('o')
        should_also_be_o        = self.scanner.get()
        self.assertEqual(should_be_o, 'o')
        self.assertEqual(should_also_be_o, 'o')
        self.assertEqual(should_be_7, 7)

    def test_find_prev(self):
        self.scanner.text       = """Jason Louis"""
        self.scanner.position   = 7
        should_be_o             = self.scanner.get()
        should_be_3             = self.scanner.find_prev('o')
        should_also_be_o        = self.scanner.get()
        self.assertEqual(should_be_o, 'o')
        self.assertEqual(should_also_be_o, 'o')
        self.assertEqual(should_be_3, 3)
