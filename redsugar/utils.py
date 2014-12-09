
class RedSource(object):
    """
    The RedSource object represents the source code file and is
    responsible for the source file's IO and reference.

    The Source object shall present
    """
    def __init__(self, filename):
        self.text = self.read(filename)

    def read(self, filename):
        with open(filename, 'r') as f:
            return f.read()


class RedLexer(object):
    """
    Lexer tokenizes redsugar source.
    """
    def __init__(self, source):
        self.text = self.remove_all_newlines(source)

    def tokenize(self):
        self.tokens = self.text.split(' ')
        self.remove_empty_tokens(self.tokens)

    def remove_all_newlines(self, text):
        return text.replace('\n', ' ')

    def remove_empty_tokens(self, tokens):
        if '' in tokens:
            tokens.remove('')
            self.remove_empty_tokens(tokens)
