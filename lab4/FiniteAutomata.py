class FiniteAutomata:
    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    def readFile(self, fileName):
        with open(fileName) as file:
            self.Q = file.readline().strip().split(' ')[2:]
            self.E = file.readline().strip().split(' ')[2:]
            self.q0 = file.readline().strip().split(' ')[2:][0]
            self.F = file.readline().strip().split(' ')[2:]
            helper = file.readline().strip().split(' ')[2:]
            source = ''
            to = ''
            destination = ''
        for token in helper:
            if '(' in token and ',' in token:
                source = token.replace('(', '').replace(',', '')
            elif ')' in token:
                to = token.replace(')', '')
            elif ';' in token:
                destination = token.replace(';', '')
                if (source, to) not in self.S.keys():
                    self.S[(source, to)] = [destination]
                else:
                    self.S[(source, to)].append(destination)

    def __str__(self):
        return "Q = { " + str(', '.join(self.Q)) + " }\n " + "E = { " + str(', '.join(self.E)) + " }\n" \
                                                                                                 "q0 = { " + str(
            ' ,'.join(self.q0)) + " }\n" + "F = { " + str(', '.join(self.F)) + " }\n" + "S = { " + str(self.S) + " }"

    def checkFDA(self):
        for k in self.S.keys():
            if len(self.S[k]) > 1:
                return False
        return True

    def checkAcceptance(self, sequence):
        if self.checkFDA():
            current = self.q0
            for each in sequence:
                if (current, each) in self.S.keys():
                    current = self.S[(current, each)][0]
                else:
                    return False
            return current in self.F
        return False
