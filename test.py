import pyneko
from pyneko import nodes
from pyneko.nodes import *
from pyneko.helpers import compile_and_run
from pyneko.xmlvisitor import XMLVisitor

from xml.etree.ElementTree import tostring

ast = Call(
        Function(['a'],
        Block(
                Call(Identifier('$print'),
                    BinaryOp('+', 
                        BinaryOp('+', 
                            Identifier('a'), 
                            LiteralInteger(5)
                        ),
                    LiteralString('\n')
                    )
                )
        )
    ),
    LiteralInteger(3)
)

FILENAME = 'test.neko'
with open(FILENAME, 'w') as f:
    f.write(tostring(XMLVisitor().make_nxml(ast)))

compile_and_run(FILENAME)
