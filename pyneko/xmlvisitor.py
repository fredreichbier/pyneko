import xml.etree.cElementTree as etree # TODO: what if there is no cElementTree, or lxml.etree ...

from .visitor import Visitor

def make_element(node, tag, add=None, **kwargs):
    """
        kwargs will be modified in-place.
    """
    if node.position:
        kwargs['p'] = node.position
    for key, value in kwargs.iteritems():
        if not isinstance(value, basestring):
            kwargs[key] = str(value)
    elem = etree.Element(tag, kwargs)
    if add is not None:
        map(elem.append, add)
    return elem

class XMLVisitor(Visitor):
    def make_nxml(self, node):
        root = etree.Element('nxml')
        root.append(self.visit(node))
        return root

    def visit_LiteralInteger(self, node):
        return make_element(node, 'i', v=node.value)

    def visit_LiteralFloat(self, node):
        return make_element(node, 'f', v=node.value)

    def visit_LiteralString(self, node):
        return make_element(node, 's', v=node.value)
    
    def visit_Identifier(self, node):
        return make_element(node, 'v', v=node.value)

    def visit_Block(self, node):
        return make_element(node, 'b',
                map(self.visit, node.children))

    def visit_Function(self, node):
        return make_element(node, 'function',
                [self.visit(node.body)],
                v=':'.join(node.args))

    def visit_BinaryOp(self, node):
        return make_element(node, 'o',
                map(self.visit, [node.e1, node.e2]),
                v=node.op)

    def visit_Call(self, node):
        return make_element(node, 'c',
                map(self.visit, [node.func] + node.args))
