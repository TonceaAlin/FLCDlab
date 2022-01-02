class ParserOutput:
    def __init__(self, non, sequence, grammar):
        self.non = non
        self.sequence = sequence
        self.grammar = grammar

    def construct_production(self):
        production_string = ''
        for each in self.non:
            if not self.grammar.isNonTerminal(each):
                production_string += each
        with open("out1.txt", "w") as file:
            file.write(production_string)
