import pyneko
from pyneko import nodes
from pyneko.nodes import *
from pyneko.helpers import compile_and_run
from pyneko.xmlvisitor import XMLVisitor

from xml.etree.ElementTree import tostring

ast = BinaryOp('=',
       Identifier('fib'),
       Function(['n'],
           If(
               BinaryOp('<=', Identifier('n'), LiteralInteger(1)),
               LiteralInteger(1),
               BinaryOp('+',
                   Call(Identifier('fib'),
                       [BinaryOp('-', Identifier('n'), LiteralInteger(1))]
                   ),
                   Call(Identifier('fib'),
                       [BinaryOp('-', Identifier('n'), LiteralInteger(2))]
                   )
               )
           )
     )
)

FILENAME = 'test.neko'
with open(FILENAME, 'w') as f:
    f.write(tostring(XMLVisitor().make_nxml(ast)))

compile_and_run(FILENAME)
