
from redsugar.regexes import regex_dictionary

class RedLexer(object):
    """
    Lexer tokenizes redsugar source.
    """
    def __init__(self, source):
        self.text       = source
        self.original   = source
        self.tokens = []

    def tokenize(self):
        #self.tokens = self.text.split(' ')
        self.remove_empty_tokens(self.tokens)

    def 





    def remove_all_newlines(self, text):
        return text.replace('\n', ' ')

    def remove_empty_tokens(self, tokens):
        if '' in tokens:
            tokens.remove('')
            self.remove_empty_tokens(tokens)

    def tokenize_double_quotes(self, tokens):
        pass  # tokenize


