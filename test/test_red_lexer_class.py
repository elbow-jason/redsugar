
import unittest
from redsugar.lexer import RedLexer

import redsugar.reserved_words as reserved_words

from testing_source_code import TESTING_SOURCE_CODE


class TestRedLexer(unittest.TestCase):

    def setUp(self):
        self.source_code = TESTING_SOURCE_CODE
        self.lexer = RedLexer(self.source_code)
        self.lexer.tokenize()

    def tearDown(self):
        pass

    def test_matcher(self):
        self.lexer.text = 'fn'
        self.lexer.match('fn')
        self.assertIn('fn', self.lexer.tokens)

    def lex_keyword(self, word, string):
        self.lexer.text = string
        self.lexer.tokenize()
        self.assertIn(word, self.lexer.tokens)

    def test_found_keyword_fn(self):
        self.lex_keyword('fn', 'fn something()\n    of the world')
        self.assertEqual(self.lexer.text, 'something()\n    of the world')

    #    def test_found_keyword_named_var(self):
    #        self.lexer.text = 'x = 1'
    #        self.lexer.tokenize()
    #        self.assertIn('x', self.lexer.tokens)
    #        self.assertEqual(self.lexer.text, '= 1')

    def test_found_keyword_indent(self):
        self.lexer.text = '    fn myshorts\n        print "on Fire"\n'
        self.lexer.tokenize()
        self.assertIn('indent', self.lexer.tokens)
        self.assertEqual(self.lexer.text, 'if "so and so says so"')

    def test_strip_left_and_right(self):
        #left
        x = self.lexer.strip_token('  x')
        self.assertEqual('x', x)
        #right
        x = self.lexer.strip_token('x   ')
        self.assertEqual('x', x)
        #both
        x = self.lexer.strip_token('   x   ')
        self.assertEqual('x', x)

    def test_remove_to_index(self):
        new_text = self.lexer.remove_to_index(0,'hello')
        #assertEqual()


class TestReservedWords(unittest.TestCase):

    def setUp(self):
        self.source_code = TESTING_SOURCE_CODE
        self.lexer = RedLexer(self.source_code)
        self.lexer.tokenize()

    def tearDown(self):
        pass

    def test_let(self):
        assert reserved_words.check('let')

    def test_randomword(self):
        assert not reserved_words.check('abcdefghijk')
