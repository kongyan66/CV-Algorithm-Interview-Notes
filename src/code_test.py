class FIB:
    def __init__(self, n):
        self.prev = 0
        self.cur = 1
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > 0:
            value = self.cur