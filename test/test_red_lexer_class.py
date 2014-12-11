
import unittest

from redsugar.lexer import RedLexer

from testing_source_code import TESTING_SOURCE_CODE


class TestRedLexer(unittest.TestCase):

    def setUp(self):
        self.source_code = TESTING_SOURCE_CODE
        self.lexer = RedLexer(self.source_code)
        self.lexer.tokenize()

    def tearDown(self):
        pass

    def test_matcher(self):
        self.lexer.text = "def end"
        self.lexer.match("def")
        self.lexer.match("end")
        self.assertIn('def', self.lexer.tokens)
        self.assertIn(
            'end',
            self.lexer.tokens,
            "\"{}\"".format(self.lexer.text)
        )

    def lex_keyword(self, word, string):
        self.lexer.text = string
        self.lexer.tokenize()
        self.assertIn(word, self.lexer.tokens)

    def test_found_keyword_end(self):
        self.lex_keyword('end', 'end of the world')
        self.assertEqual(self.lexer.text, 'of the world')

    def test_found_keyword_fn(self):
        self.lex_keyword('fn', 'fn something()\nof the world')
        self.assertEqual(self.lexer.text, 'of the world')

    def test_found_keyword_end(self):
        self.lex_keyword('end', 'end of the world')
        self.assertEqual(self.lexer.text, 'of the world')

    def test_found_keyword_end(self):
        self.lex_keyword('end', 'end of the world')
        self.assertEqual(self.lexer.text, 'of the world')

    def test_found_keyword_end(self):
        self.lex_keyword('end', 'end of the world')
        self.assertEqual(self.lexer.text, 'of the world')
