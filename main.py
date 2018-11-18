execfile("./helpers.py")
execfile("./Transaction.py")
execfile("./Checkpoint.py")

class LogParser:
    def __init__(self, inputFile):
        self.vars = {}
        self.transactions = {}
        self.ckpts = []
        self.commited = []

        self.inputFile = inputFile
        self.inputData = self.getFileContent(inputFile)
        
        self.setVars(self.inputData[0])
        print "Valores antes da transacao:"
        print "\t%s" % str (self.vars)

        self.iterateInput()

        print "Valores depois da transacao:"
        print "\t%s" % str (self.vars)

    def iterateInput(self):        
        for lineIndex, lineValue in enumerate(self.inputData):
            lineIndex = lineIndex+1
            lineValue = self.clearString(lineValue, "linha")

            if "start" in lineValue:
                # comeco de checkpoint
                if "ckpt" in lineValue:
                    lineValue = self.clearString(lineValue, "ckpt")

                    ckptTransactions = lineValue.split(',')
                    ckpt = Checkpoint(lineIndex, ckptTransactions)
                    
                    self.ckpts.append(ckpt)

                # comeco de transacao
                else:
                    lineSplit = lineValue.split('start ')
                    t = Transaction(lineSplit[1], lineIndex)

                    self.transactions[lineSplit[1]] = t
            
            elif "commit" in lineValue:
                lineSplit = lineValue.split('commit ')
                self.commited.append(lineSplit[1])

                # passa valor das variaveis da transacao para variavel final
                for key in self.transactions[lineSplit[1]].vars:
                    self.vars[key.upper()] = self.transactions[lineSplit[1]].vars[key]

            elif "end" in lineValue:
                for ckpt in self.ckpts:
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

            # array associativo onde a chave eh o nome da var
            self.vars[varSplit[0]] = varSplit[1]

    def clearString(self, string, tipo):
        string = string.lower()

        if tipo == "linha":
            string = string.replace("<","")
            string = string.replace(">","")
        elif tipo == "ckpt":
            string = string.replace("start ckpt(","")
            string = string.replace(")","")

        return string

    def getFileContent(self, pathAndFileName):
        with open(pathAndFileName, 'r') as theFile:
            data = theFile.read().split('\n')
            return data

log1 = LogParser("./teste1")
# log2 = LogParser("./teste2")

# print_obj(log1)
# print_obj(log2)

