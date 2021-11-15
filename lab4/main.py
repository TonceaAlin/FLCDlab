# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from FiniteAutomata import *


def displayMenu():
    print("1.Read FA from file")
    print("2.Show FA")
    print("3.Show states")
    print("4.Show alphabet")
    print("5.Show transition functions")
    print("6.Show final states")
    print("7.Check DFA")
    print("8.Check a sequence")

def run():
    finite = FiniteAutomata([], [], '', [], {})
    while True:
        displayMenu()
        print(">>>")
        x = int(input())
        if x == 1:
            finite.readFile("FA.in")
        elif x == 2:
            print(finite)
        elif x == 3:
            print(finite.Q)
        elif x == 4:
            print(finite.E)
        elif x == 5:
            print(finite.S)
        elif x == 6:
            print(finite.F)
        elif x == 7:
            print(finite.checkFDA())
        elif x == 8:
            sequence = input("sequence: ")
            print(finite.checkAcceptance(sequence))
        else:
            break

if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
