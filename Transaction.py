class Transaction:
    def __init__(self, name, startLine):
        self.name = name        
        self.startLine = startLine
        self.vars = {}
    