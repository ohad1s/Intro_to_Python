class File():
    def __init__(self,name):
        self.name=name
        self.isOpen=False

    def __repr__(self):
        return f"file name: {self.name}, isOpen?: {self.isOpen}"

    def isOpen(self):
        return self.isOpen

    def open(self):
        self.isOpen=True

    def close(self):
        self.isOpen=False



