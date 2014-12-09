

class RedScanner(object):
    """
    RedScanner is a scanner. It goes back and forth.
    """

    def __init__(self, text):
        self.text = text
        self.position = 0
        self.marker = 0

    def goto(self, position):
        self.position = position

    def get(self):
        return self.text[self.position]

    def next(self):
        self.position += 1

    def prev(self):
        self.position -= 1

    def mark(self):
        self.marker = self.position

    def diff(self):
        return self.position - self.marker

    def find_next(self, char):
        self.next()
        current = self.get()
        while current != char:
            self.next()
            current = self.get()
        return self.position

    def find_prev(self, char):
        self.prev()
        current = self.get()
        while current != char:
            self.prev()
            current = self.get()
        return self.position
