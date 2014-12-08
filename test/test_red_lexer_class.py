
import unittest

from redsugar.utils import RedLexer


class TestRedLexer(unittest.TestCase):

    def setUp(self):
        self.source_code = """
        fn hello
            print "hello world"
        end
        """
        self.lexer = RedLexer(self.source_code)

    def tearDown(self):
        pass

    def test_redscanner_tokenize(self):
        self.lexer.tokenize()
        self.assertEqual(self.tokens[0], 'fn')
