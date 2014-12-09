

class RedSourcer(object):
    """
    The RedSource object represents the source code file and is
    responsible for the source file's IO and reference.

    The Source object shall read the redsugar source file.
    """
    def __init__(self, filepath):
        self.path = filepath

    def read(self, filename):
        with open(filename, 'r') as f:
            return f.read()
