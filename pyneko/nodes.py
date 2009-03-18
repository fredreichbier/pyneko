class Node(object):
    def __init__(self):
        self.position = ':' 
        # workaround, see http://lists.motion-twin.com/pipermail/neko/2009-January/002481.html

class LiteralInteger(Node):
    def __init__(self, value=0):
        Node.__init__(self)
        self.value = value

class LiteralFloat(Node):
    def __init__(self, value=0.0):
        Node.__init__(self)
        self.value = value

class LiteralString(Node):
    def __init__(self, value=''):
        Node.__init__(self)
        self.value = value

class Identifier(Node):
    def __init__(self, value=''):
        Node.__init__(self)
        self.value = value

class Block(Node):
    def __init__(self, children):
        Node.__init__(self)
        self.children = children

    def add_child(self, node):
        self.children.append(node)

class Parenthesis(Node):
    def __init__(self, child):
        Node.__init__(self)
        self.child = child 

class FieldAccess(Node):
    def __init__(self, obj, field):
        Node.__init__(self)
        self.obj = obj
        self.field = field

class Call(Node):
    def __init__(self, func_node, args):
        Node.__init__(self)
        self.func = func_node
        self.args = args

class ArrayAccess(Node):
    def __init__(self, elem, index):
        Node.__init__(self)
        self.elem = elem
        self.index = index

class Var(Node):
    def __init__(self, vars):
        """
            :param vars: a dictionary 
                         {name (python str): value (ast node or None) }
        """
        Node.__init__(self)
        self.vars = vars

class While(Node):
    def __init__(self, cond, body):
        Node.__init__(self)
        self.cond = cond
        self.body = body

class DoWhile(Node):
    def __init__(self, cond, body):
        Node.__init__(self)
        self.cond = cond
        self.body = body

class If(Node):
    def __init__(self, cond, body, else_body=None):
        Node.__init__(self)
        self.cond = cond
        self.body = body
        self.else_body = else_body

class BinaryOp(Node):
    def __init__(self, op, e1, e2):
        Node.__init__(self)
        self.op = op
        self.e1 = e1
        self.e2 = e2

class Try(Node):
    def __init__(self, value, try_, catch):
        """
            :param value: The exception name to catch
            :param try_: The statement to try
            :param catch: The statement to be executed if *value* was caught.
        """
        Node.__init__(self)
        self.value = value
        self.try_ = try_
        self.catch = catch

class Function(Node):
    def __init__(self, args, body):
        Node.__init__(self)
        self.args = args
        self.body = body

class Return(Node):
    def __init__(self, value=None):
        Node.__init__(self)
        self.value = value

class Break(Node):
    def __init__(self, value=None):
        Node.__init__(self)
        self.value = value

class Continue(Node):
    pass

class Next(Node):
    def __init__(self, e1, e2):
        Node.__init__(self)
        self.e1 = e1
        self.e2 = e2

class Label(Node):
    def __init__(self, label):
        """
            :param label: the label name as string
        """
        Node.__init__(self)
        self.label = label

class Switch(Node):
    def __init__(self, control, conditions):
        """
            :param control: The control variable node of the switch statement.
            :param conditions: a dict {cond node: body node} of cases,
                               cond node = 'default' is the default option.
        """
        Node.__init__(self)
        self.control = control
        self.conditions = conditions

class Object(Node):
    def __init__(self, members):
        """
            Object literal
            :param members: a dictionary of {name: node}
        """
        Node.__init__(self)
        self.members = members

class Neko(Node):
    def __init__(self, code):
        Node.__init__(self)
        self.code = code

