
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
            'string': self.tokens.append,
        }

        self.regexes = {
        'def':      r'def ',
        'end':      r'end(\s|\z)',
        'newline':  r'\n^',
        'string':   r'".*"',
        }

    def tokenize(self):
        self.match('def')
        self.remove_empty_tokens(self.tokens)

    def match(self, key):
        result = re.match(self.regexes[key], self.text)
        if result is not None:
            result = result.group(0)
            result = self.special_keywords.get(key, result)
            self.tokens.append(result)

    def remove_by_regex(self, key):
        re.sub(self.regexes[key], '', self.text)

    def remove_all_newlines(self, text):
        return text.replace('\n', ' ')

    def remove_empty_tokens(self, tokens):
        if '' in tokens:
            tokens.remove('')
            self.remove_empty_tokens(tokens)

    def tokenize_double_quotes(self, tokens):
        pass  # tokenize
