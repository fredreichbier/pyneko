import lxml.etree as etree

from .visitor import Visitor

def make_element(node, tag, add=None, text='', **kwargs):
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
    if text:
        elem.text = text
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

    def visit_Parenthesis(self, node):
        return make_element(node, 'p',
                self.visit(node.child))

    def visit_FieldAccess(self, node):
        return make_element(node, 'g',
                [self.visit(node.obj)], v=node.field)

    def visit_Call(self, node):
        return make_element(node, 'c',
                map(self.visit, [node.func] + node.args))

    def visit_ArrayAccess(self, node):
        return make_element(node, 'a',
                [self.visit(node.elem), self.visit(node.index)])

    def visit_Var(self, node):
        declarations = []
        for name, var in node.vars.iteritems():
            if var is not None:
                declarations.append(
                     make_element(node, 'v',
                         self.visit(var),
                         name=name
                    )
                )
            else:
                declarations.append(
                        make_element(node, 'v',
                            name=name
                        )
                )
        return make_element(node, 'var', declarations)

    def visit_While(self, node):
        return make_element(node, 'while',
                [self.visit(node.cond),
                self.visit(node.body)]
                )

    def visit_DoWhile(self, node):
        return make_element(node, 'do',
                [self.visit(node.body),
                self.visit(node.cond)]
                )

    def visit_If(self, node):
        args = [self.visit(node.cond), self.visit(node.body)]
        if node.else_body is not None:
            args.append(self.visit(node.else_body))
        return make_element(node, 'if', args)

    def visit_BinaryOp(self, node):
        return make_element(node, 'o',
                map(self.visit, [node.e1, node.e2]),
                v=node.op)

    def visit_Try(self, node):
        return make_node(node,
                [self.visit(node.try_), self.visit(node.catch)],
                v=node.value)

    def visit_Function(self, node):
        return make_element(node, 'function',
                [self.visit(node.body)],
                v=':'.join(node.args))

    def visit_Return(self, node):
        if node.value is not None:
            return make_element(node, 'return', [self.visit(node.value)])
        else:
            return make_element(node, 'return')

    def visit_Break(self, node):
        if node.value is not None:
            return make_element(node, 'break', [self.visit(node.value)])
        else:
            return make_element(node, 'break')

    def visit_Continue(self, node):
        return make_element(node, 'continue')

    def visit_Next(self, node):
        return make_element(node, 'next',
                [self.visit(node.e1), self.visit(node.e2)])

    def visit_Label(self, node):
        return make_element(node, 'label', v=node.label)

    def visit_Switch(self, node):
        nodes = [self.visit(node.control)]
        for name, exp in node.conditions.iteritems():
            if name == 'default':
                nodes.append(
                        make_element(node, 'default',
                            [self.visit(exp)]
                        )
                )
            else:
                nodes.append(
                        make_element(node, 'case',
                            [self.visit(name),
                                self.visit(exp)]
                        )
                )
        return make_element(node, 'switch', nodes)

    def visit_Object(self, node):
        elems = []
        for name, member_node in node.members:
            elems.append(
                    make_element(node, 'v',
                        [self.visit(member_node)],
                        v=name)
                    )
        return make_element(node, 'object', elems)

    def visit_Neko(self, node):
        return make_element(node, 'neko',
                text=node.code)


