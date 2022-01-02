import functools
import operator

from ParserOutput import ParserOutput


class Parser2:
    def __init__(self, grammar, sequence):
        self.grammar = grammar
        self.state = 'q'
        self.index = 1
        self.workingStack = []
        self.inputStack = grammar.getInitialState()
        self.sequence = sequence

    def expand(self):
        self.workingStack.append((self.inputStack[0][0], 1))
        self.inputStack[0] = self.inputStack[0].replace(self.inputStack[0][0], self.grammar.getNthProduction(self.inputStack[0][0], 1)[1], 1)

    def back(self):
        symbol = self.workingStack[-1]
        self.index -= 1
        self.inputStack[0] = symbol + self.inputStack[0]
        self.workingStack = self.workingStack[:-1]

    def advance(self):
        symbol = self.inputStack[0][0]
        self.workingStack.append(symbol)
        self.inputStack[0] = self.inputStack[0][1:]
        self.index += 1

    def momentary_insuccess(self):
        self.state = 'b'

    def another_try(self):
        symbol = self.workingStack[-1] # S1 => 1

        if symbol[1] < len(self.grammar.P[symbol[0]]): # <- S = a | b | c = { S : [a, b, c] }
            self.state = 'q'
            newSymbol = self.grammar.getNthProduction(symbol[0], symbol[1] + 1)  # (S, aS)
            self.inputStack = [x.replace(self.grammar.getNthProduction(symbol[0], int(symbol[1]))[1],
                                         newSymbol[1], 1) for x in self.inputStack]
            self.workingStack[-1] = (symbol[0], symbol[1]+1)
        else:
            self.state = 'b'
            self.workingStack = self.workingStack[:-1]
            self.inputStack = [x.replace(self.grammar.getNthProduction(symbol[0], symbol[1])[1], symbol[0], 1) for x in self.inputStack]


    def success(self):
        self.state = 'f'

    def printParser(self):
        print(self.state, '\nindex', self.index, "\nalpha - working", self.workingStack, "\nbeta - input ", self.inputStack)

    def parse(self):
        self.printParser()
        while self.state != 'f' and self.state != 'e':
            if self.state == 'q':
                if self.index == len(self.sequence)+1 and len(self.inputStack) == 1 and self.inputStack[0] == '':
                    self.success()
                    print("successfully parsed")
                elif self.grammar.isNonTerminal(self.inputStack[0][0]):
                    print("expand")
                    self.expand()
                elif self.index - 1 >= len(self.sequence):
                    print("momentary insuccess")
                    self.momentary_insuccess()
                elif self.grammar.isTerminal(self.inputStack[0][0]) and self.inputStack[0][0] == self.sequence[self.index-1]:
                    print("advance")
                    self.advance()
                else:
                    print("momentary insuccess")
                    self.momentary_insuccess()
            elif self.state == 'b':
                if self.grammar.isTerminal(self.workingStack[-1]):
                    self.back()
                    print("going back")
                else:
                    print("another try")
                    self.another_try()
        if self.state == 'e':
            print("Error while parsing")
        else:
            print("Sequence accepted!")
            self.buildProductions()

    def buildProductions(self):
        parseTree = '\nParse result: '
        copy = ''
        for each in self.workingStack:
            if type(each) == tuple:
                copy += '{0}{1}'.format(each[0], each[1])
        parseTree += copy
        print(parseTree)
        output = ParserOutput(copy, self.sequence, self.grammar)
        output.construct_production()

