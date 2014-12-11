
import re


class RedLexer(object):
    """
    Lexer tokenizes redsugar source.
    """
    def __init__(self, source):
        self.text       = source
        self.original   = source
        self.tokens = []
        self.special_keywords = {
            'string': self.string,
        }

        self.regexes = {
        'fn':      r'\Afn ',
        #'end':      r'\A[e][n][d][(\n|\z)]',

        'newline':  r'\n^',
        'string':   r'".*"',
        'named_var': r'[a-zA-Z_][a-zA-Z0-9_]*\s'
        }

    def string(self, matched):
        return matched

    def tokenize(self):
        self.match('def')
        self.match('end')
        self.remove_empty_tokens(self.tokens)

    def match(self, key):
        result = re.match(self.regexes[key], self.text)
        if result is not None:
            function = self.special_keywords.get(key, key)
            if function is not key:
                result = function(result)
            else:
                result = key
            self.tokens.append(result)
            self.text = self.remove_by_regex(key, self.text)
            self.text.lstrip()

    def remove_by_regex(self, key, text):
        return re.sub(self.regexes[key], '', text)

    def remove_all_newlines(self, text):
        return text.replace('\n', ' ')

    def remove_empty_tokens(self, tokens):
        if '' in tokens:
            tokens.remove('')
            self.remove_empty_tokens(tokens)

    def tokenize_double_quotes(self, tokens):
        pass  # tokenize
