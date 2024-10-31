import sys
from antlr4 import *
from DOTLexer import DOTLexer
from DOTParser import DOTParser
from DOTVisitor import DOTVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DOTLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DOTParser(stream)
    tree = parser.graph()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = DOTVisitor()
        vinterp.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
