class FiniteAutomata:
    @staticmethod
    def readFile(fileName):
        with open(fileName) as file:
            Q = FiniteAutomata.parseLine(file.readline())
            E = FiniteAutomata.parseLine(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = FiniteAutomata.parseLine(file.readline())
            S = FiniteAutomata.parseTransitions(FiniteAutomata.parseLine(''.join([line for line in file])))
            return FiniteAutomata(Q, E, S, q0, F)

    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F

    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def parseTransitions(parts):
        result=[]
        transitions=[]
        index=0

        while index<len(parts):
            transitions.append(parts[index]+','+parts[index+1])
            index+=2

        for transition in transitions:
            lhs,rhs=transition.split('->')
            state2=rhs.strip()
            state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]
            result.append(((state1, route), state2))
        return result
    def printQ(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }\n'
    def printE(self):
        return 'E = { ' + ', '.join(self.E) + ' }\n'
    def printS(self):
        return 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n'
    def printq0(self):
        return 'q0 = ' + str(self.q0) + '\n'
    def printF(self):
        return 'F = { ' + ', '.join(self.F) + ' }\n'
    def __str__(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n'