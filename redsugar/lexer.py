
import re
import reserved_words

class RedLexer(object):
    """
    Lexer tokenizes redsugar source.
    """
    def __init__(self, source):
        self.text       = source
        self.original   = source
        self.tokens = []
        self.special_keywords = {
            'string': self.the_same,
            'named_var': self.the_same,
            'indent': self.indent,
            'newline': self.newline
        }

        self.regexes = {
        'fn':      r'\Afn ',
        #'end':      r'\A[e][n][d][(\n|\z)]',

        'newline':  r'\n',
        'string':   r'".*"',
        'named_var': r'[a-zA-Z_][a-zA-Z0-9_]*\s',
        'indent'    : r'    '
        }

    def named_var(self, matched):
        if matched in reserved_words.reserved_words:
            e = "Matched Word was Reserved, but was somehow missed by the transpiler."
            raise Exception(e)
        return matched

    def the_same(self, matched):
        print "STRING OR NAMED VAR LITERAL", matched
        return matched

    def indent(self, matched):
        return 'indent'

    def newline(self, matched):
        return 'newline'

    def strip_token(self, found):
        found = found.lstrip()
        found = found.rstrip()
        return found

    def tokenize(self):
        self.match('string')
        self.match('newline')
        self.match('indent')
        self.match('fn')
        self.match('named_var')
        self.remove_empty_tokens(self.tokens)

    def match(self, key):
        regex = self.regexes.get(key, None)
        if regex is None:
            x = """
Tried to match an undefined token. \
There is no regex associated with the key '{}'.""".format(key)
            raise Exception(x)
        regex_match = re.match(regex, self.text)
        if regex_match is not None:
            function = self.special_keywords.get(key, key)
            if function is not key:
                result = function(regex_match.group(0))
                print "FOUND SPECIAL WORD:", result
            else:
                result = key
                print "FOUND WORD:", result
            result = self.strip_token(result)
            self.tokens.append(result)
            self.text = self.remove_by_regex(key, self.text)
            self.text.lstrip()
        else:
            print "text:", self.text, "\nFIRST WORD WAS NOT:", key

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
