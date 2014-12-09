
import unittest

from redsugar.utils import RedLexer

TESTING_SOURCE_CODE = """
fn hello
    print "hello world"
end
"""


class TestRedLexer(unittest.TestCase):

    def setUp(self):
        self.source_code = TESTING_SOURCE_CODE
        self.lexer = RedLexer(self.source_code)
        self.lexer.tokenize()

    def tearDown(self):
        pass

    def test_tokenize_makes_list(self):
        self.assertIs(list, type(self.lexer.tokens))

    def test_tokenize_removes_newlines(self):
        for item in self.lexer.tokens:
            self.assertNotIn('\n', item)

    def test_tokenize_content_is_as_expected(self):
        self.assertEqual(self.lexer.tokens[0], 'fn')
        self.assertEqual(self.lexer.tokens[1], 'hello')
        self.assertEqual(self.lexer.tokens[2], 'print')
        self.assertEqual(
            self.lexer.tokens[3],
            '"',
            "first single quote not alone"
        )
        self.assertEqual(self.lexer.tokens[4], "hello")
        self.assertEqual(
            self.lexer.tokens[3],
            '"',
            "second single quote not alone"
        )
        self.assertEqual(self.lexer.tokens[2], 'end')

    def test_remove_empty_tokens(self):
        self.assertNotIn('', self.lexer.tokens)
