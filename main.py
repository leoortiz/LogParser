# coding=utf-8
# python 2.7
# 
# Alunos:
# - Leonardo Ortiz
# - Daniel Welter

execfile("./helpers.py")
execfile("./Transaction.py")
execfile("./Checkpoint.py")

class LogParser:
    def __init__(self, inputFile):
        self.vars = {} # variaveis da transação
        self.transactions = {} # transações do log
        self.ckpts = [] # checkpoints do log
        self.commited = [] # armazena transações que fizeram commit

        self.inputFile = inputFile # nome do arquivo de entrada (teste1 e teste2)
        self.inputData = self.getFileContent(inputFile) # conteúdo do arquivo de entrada como lista
        
        self.setVars(self.inputData[0]) # seta as variaveis
        print "Valores antes da transacao:"
        print "\t%s" % str (self.vars)

        self.iterateInput()

        print "Valores depois da transacao:"
        print "\t%s" % str (self.vars)

    def iterateInput(self):
        for lineIndex, lineValue in enumerate(self.inputData):
            lineIndex = lineIndex+1 # para contabilizar linha. quando 0 = linha 1, etc
            lineValue = self.clearString(lineValue, "linha") # pega o conteúdo da linha sem caracteres desnecessários

            # se tiver "start" na linha
            if "start" in lineValue:

                # se tiver "ckpt" indica começo de checkpoint
                if "ckpt" in lineValue:
                    # limpa "ckpt" para manter apenas transações do checkpoint
                    lineValue = self.clearString(lineValue, "ckpt")

                    # array das transações do checkpoint(ex: ['t1','t2'])
                    ckptTransactions = lineValue.split(',')
                    # cria novo checkpoint(objeto)
                    ckpt = Checkpoint(lineIndex, ckptTransactions)

                    # armazena checkpoint no LogParser
                    self.ckpts.append(ckpt)

                # comeco de transacao
                else:
                    # tira 'start' para manter apenas nome da transação
                    lineSplit = lineValue.split('start ')

                    # cria nova transação(nome, linha que começa)
                    t = Transaction(lineSplit[1], lineIndex)

                    # armazena transação no LogParser
                    self.transactions[lineSplit[1]] = t
            
            # tem commit
            elif "commit" in lineValue:
                # separa valores
                lineSplit = lineValue.split('commit ')
                
                #armazena transação em lista de "commitados"
                self.commited.append(lineSplit[1])

                # passa valor das variaveis da transacao para variaveis alterados no Log
                for key in self.transactions[lineSplit[1]].vars:
                    self.vars[key.upper()] = self.transactions[lineSplit[1]].vars[key]

            # se end, indica fim de checkpoint
            elif "end" in lineValue:
                # percorre checkpoints do log
                for ckpt in self.ckpts:
                    # se endLine do checkpoint for 0, checkpoint ainda não acabou
                    if ckpt.endLine == 0:
                        ckpt.endLine = lineIndex

            # atribuicao de valores
            elif "|" not in lineValue:
                action = lineValue.split(',')
                var = action[1]

                self.transactions[action[0]].vars[var] = action[2]

    def setVars(self, vars):
        vars = vars.split(" | ")

        for i, var in enumerate(vars):
            varSplit = var.split("=")

            # dicionario onde a chave eh o nome da var
            self.vars[varSplit[0]] = varSplit[1]

    def clearString(self, string, tipo):
        string = string.lower()

        if tipo == "linha": #se for escrita (write)
            string = string.replace("<","") #remove <
            string = string.replace(">","") #remove >
        elif tipo == "ckpt": #se for um checkpoint
            #remove os caracteres do ckpt e deixa apenas as transações envolvidas
            string = string.replace("start ckpt(","") 
            string = string.replace(")","") 

        return string

    def getFileContent(self, pathAndFileName):
        # abre arquivo no modo leitura
        with open(pathAndFileName, 'r') as theFile:
            # separa linhas do arquivo em lista
            data = theFile.read().split('\n')

            #retorna lista
            return data

print "Teste 1:"
log1 = LogParser("./teste01")

print "\nTeste 2:"
log2 = LogParser("./teste02")