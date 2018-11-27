# coding=utf-8
# python 2.7
# 
# Alunos:
# - Leonardo Ortiz
# - Daniel Welter
# Apresentação
# https://docs.google.com/presentation/d/1RIf1WofLys628svTFFoB0JdE_Jk12tWN61XM38ulXi8/edit?usp=sharing

class Checkpoint:
    def __init__(self, startLine, transactions):
        self.startLine = startLine
        self.endLine = 0
        self.transactions = transactions