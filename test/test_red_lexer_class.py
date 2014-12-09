
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
        self.lexer.match()

    def test_found_keyword_def(self):
        self.lexer.tokenize()
        self.assertIn('def', self.lexer.tokens)

    def test_removal_of_preceding_space_per_line(self):
        self.assertEqual(self.lexer.original, TESTING_SOURCE_CODE)
        self.assertNotIn('\n ', self.lexer.text)

    def test_found_keyword_print(self):
        self.lexer.tokenize()
        self.assertIn('print', self.lexer.tokens)

    def test_found_keyword_end(self):
        self.lexer.tokenize()
        self.assertIn('end', self.lexer.tokens)

    def test_tokenize_makes_list(self):
        self.assertIs(list, type(self.lexer.tokens))

    def test_remove_all_newlines(self):
        test_string = "I\nhave\nno\nnewlines"
        no_newlines = self.lexer.remove_all_newlines(test_string)
        self.assertNotIn('\n', no_newlines)

    def test_tokenize_removes_newlines(self):
        for item in self.lexer.tokens:
            self.assertNotIn('\n', item)

    def test_tokenize_content_is_as_expected(self):
        self.assertEqual(self.lexer.tokens[0], 'def')
        self.assertEqual(self.lexer.tokens[1], 'hello')
        self.assertEqual(self.lexer.tokens[2], 'print')

    def test_tokenized_list_ends_with_end(self):
        self.assertEqual(self.lexer.tokens[-1], 'end')

    def test_remove_empty_tokens(self):
        self.assertNotIn('', self.lexer.tokens)
