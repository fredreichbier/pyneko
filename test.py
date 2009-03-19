import pyneko
from pyneko import nodes
from pyneko.nodes import *
from pyneko.helpers import compile_and_run
from pyneko.xmlvisitor import XMLVisitor

from xml.etree.ElementTree import tostring

# equivalent to:
# greet = function(what)
#    $print(("Hello " + what) + "!\n")
# greet("Neko");
# -> Hello Neko!

ast = Block([
        BinaryOp('=',
            Identifier('greet'),
            Function(['what'],
                Call(
                    Identifier('$print'),
                    [
                        BinaryOp('+',
                            BinaryOp('+',
                                LiteralString('Hello '),
                                Identifier('what')
                            ),
                            LiteralString('!\n')
                        )
                    ]
                    )
                )
            ),
        Call(
            Identifier('greet'),
            [LiteralString('Neko')]
            )
        ])


FILENAME = 'test.neko'
with open(FILENAME, 'w') as f:
    f.write(tostring(XMLVisitor().make_nxml(ast)))

compile_and_run(FILENAME)
