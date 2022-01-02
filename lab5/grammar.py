

class Grammar:
    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.S = S
        self.P = P

    def readFile(self, fileName):
        with open(fileName) as file:
            self.N = file.readline().replace('}', '').strip().split(' ')[3:]
            self.E = file.readline().replace('}', '').strip().split(' ')[3:]
            helper = file.readline()[3:].replace(' ', '').replace('{', '').replace('}', '').strip().split(',')
            self.S = file.readline().replace('}', '').strip().split(' ')[2:]
        for token in helper:
            items = token.split('->')
            if '|' in items[1]:
                after = items[1].split('|')
            else:
                after = items[1]
            if items[0] not in self.P.keys():
                self.P[items[0]] = []
            for x in after:
                self.P[items[0]].append(x)

    def checkCFG(self):
        for each in self.P.keys():
            for x in self.E:
                if x in each:
                    return False
            for nonterminal in each:
                if nonterminal not in self.N:
                    return False
            for seq in self.P[each]:
                for symbol in seq:
                    if symbol not in self.N and symbol not in self.E:
                        return False
        return True

    def nonterminalsProductions(self, symbol):
        print(self.P[symbol])

    def isNonTerminal(self, symbol):
        if symbol in self.N:
            return True
        return False

    def isTerminal(self, symbol):
        if symbol in self.E:
            return True
        return False

    def getNthProduction(self, key, index):
        return key, self.P[key][index - 1]

    def getInitialState(self):
        return self.S

