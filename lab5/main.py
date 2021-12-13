# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from grammar import Grammar
from parser2 import Parser2


def run():
    gram = Grammar([], [], {}, [])
    gram.readFile("g1.txt")
    # print(gram.checkCFG())
    # sym = input(">>")
    # gram.nonterminalsProductions(sym)
    parser = Parser2(gram, "aacbc")
    parser.parse()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
