"""
Reserved Words may not be used in redsugar due to collisions with the target language
"""

not_allowed = [
    'let'
]


def check(word):
    return word in not_allowed
