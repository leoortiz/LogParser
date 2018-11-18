class Checkpoint:
    def __init__(self, startLine, transactions):
        self.startLine = startLine
        self.endLine = 0
        self.transactions = transactions