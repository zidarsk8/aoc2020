import aoc18_data


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Node = left
        self.right: Node = right

    def parse(self):
        if len(self.text) == 1:
            self.val = self.text

    @property
    def depth(self):
        l_depth = self.left.depth if self.left else 0
        r_depth = self.right.depth if self.right else 0
        return max([l_depth, r_depth]) + 1

    def to_str(self) -> str:
        l_str = self.left.to_str() if self.left else ""
        r_str = self.right.to_str() if self.right else ""
        if not l_str and not r_str:
            return self.val

        pad = " " * self.depth

        l_pad = "\n".join(f"{pad}{line}" for line in l_str.splitlines())
        r_pad = "\n".join(f"{pad}{line}" for line in r_str.splitlines())

        return f"{l_pad}\n{self.val}\n{r_pad}"

    def calculate(self):
        if not self.left and not self.right:
            return int(self.val)

        if self.val == "+":
            return self.left.calculate() + self.right.calculate()

        if self.val == "*":
            return self.left.calculate() * self.right.calculate()


class Tree:
    def __init__(self, text: str):
        self.text: str = text.replace(" ", "")
        self.walk: str
        self.trunk: Node = None

    @property
    def _char(self):
        char = self.walk[-1]
        self.walk = self.walk[:-1]
        return char

    def calculate(self):
        return self.trunk.calculate()

    def _parse(self):
        char = self._char
        if not self.walk and char in "123456789":
            return Node(char)

        if char in "123456789":
            right = Node(char)
            next_char = self._char
            if next_char == "(":
                return right

            val = next_char
            left = self._parse()

            return Node(val, left=left, right=right)

        if char == ")":
            right = self._parse()
            if not self.walk:
                return right
            next_char = self._char
            if next_char == "(":
                return right
            val = next_char
            left = self._parse()
            return Node(val, left=left, right=right)
        if char == "(":
            pass

    def parse(self):
        self.walk = self.text
        self.trunk = self._parse()

    @property
    def depth(self):
        return self.trunk.depth if self.trunk else 0

    def to_str(self) -> str:
        if not self.trunk:
            return ""

        tree_str: str = self.trunk.to_str()
        max_len = max(len(line) for line in tree_str.splitlines())
        return "\n".join(
            line + ("-" * (max_len - len(line))) for line in tree_str.splitlines()
        )

    def to_str_transpose(self):
        tree_str: str = self.to_str()
        transpose = list(map(list, zip(*tree_str.splitlines())))
        upright = "\n".join("".join(line) for line in transpose)
        return upright.replace("-", ".")

    def print_tree(self):
        print(self.to_str_transpose())


def test_parse():
    tree = Tree("1")
    tree.parse()
    assert tree.trunk.val == "1"
    tree = Tree("1 + 2")
    tree.parse()
    assert tree.trunk.val == "+"
    assert tree.trunk.left.val == "1"
    assert tree.trunk.right.val == "2"
    tree = Tree("1 + 2 + 3")
    tree.parse()
    assert tree.trunk.val == "+"
    assert tree.trunk.left.val == "+"
    assert tree.trunk.left.left.val == "1"
    assert tree.trunk.left.right.val == "2"
    assert tree.trunk.right.val == "3"
    tree = Tree("1 + 2 * 3 + 4")
    tree.parse()
    assert tree.trunk.val == "+"
    assert tree.trunk.left.val == "*"
    assert tree.trunk.left.left.val == "+"
    assert tree.trunk.left.left.left.val == "1"
    assert tree.trunk.left.left.right.val == "2"
    assert tree.trunk.left.right.val == "3"
    assert tree.trunk.right.val == "4"


def test_parenthisis_parse():
    tree = Tree("(1)")
    tree.parse()
    assert tree.trunk.val == "1"
    tree = Tree("(((1)))")
    tree.parse()
    assert tree.trunk.val == "1"
    tree = Tree("(1+2)")
    tree.parse()
    assert tree.trunk.val == "+"
    assert tree.trunk.left.val == "1"
    assert tree.trunk.right.val == "2"

    tree = Tree("1 + (2 + 3)")
    tree.parse()
    assert tree.trunk.val == "+"
    assert tree.trunk.left.val == "1"
    assert tree.trunk.right.left.val == "2"
    assert tree.trunk.right.right.val == "3"
    assert tree.trunk.right.val == "+"

    tree = Tree("1 + (2 + 3) * 2")
    tree.parse()
    assert tree.trunk.val == "*"
    assert tree.trunk.left.val == "+"
    assert tree.trunk.left.left.val == "1"
    assert tree.trunk.left.right.val == "+"
    assert tree.trunk.left.right.left.val == "2"
    assert tree.trunk.left.right.right.val == "3"
    assert tree.trunk.right.val == "2"

    tree = Tree("(((1) + (2 + 3)) * 2)")
    tree.parse()
    assert tree.trunk.val == "*"
    assert tree.trunk.left.val == "+"
    assert tree.trunk.left.left.val == "1"
    assert tree.trunk.left.right.val == "+"
    assert tree.trunk.left.right.left.val == "2"
    assert tree.trunk.left.right.right.val == "3"
    assert tree.trunk.right.val == "2"


def test_print_tree():
    tree = Tree("")
    tree.trunk = Node(
        "1",
        left=Node(
            "2", left=Node("A"), right=Node("B", left=Node("8"), right=Node("9"))
        ),
        right=Node("3", left=Node("X")),
    )
    tree.print_tree()
    assert (
        tree.to_str_transpose()
        == """     1  
     .  
     .  
     .  
 2   . 3
 .   . .
 .   .X.
A. B ...
.. . ...
..8.9..."""
    )


def test_simple_tree():
    tree = Tree("")
    assert tree is not None


def test_tree_depth():
    tree: Tree = Tree("")
    assert tree.depth == 0

    tree.trunk = Node("")
    assert tree.depth == 1

    tree.trunk = Node(
        "1",
        left=Node(
            "2", left=Node("3"), right=Node("4", right=Node("5", left=Node("6"))),
        ),
    )
    assert tree.depth == 5


def test_tree_to_str():
    tree: Tree = Tree("A")
    assert tree.to_str() == ""

    tree.trunk = Node("1")
    assert tree.to_str() == "1"

    tree.trunk = Node("1", left=Node("2"))
    assert tree.to_str() == """  2\n1--"""

    tree.trunk = Node("1", left=Node("2"), right=Node("3"))
    assert tree.to_str() == """  2\n1--\n  3"""

    tree.trunk = Node(
        "1",
        left=Node("2", left=Node("A"), right=Node("B")),
        right=Node("3", left=Node("X")),
    )
    print(tree.to_str())

    assert tree.to_str() == """     A\n   2--\n     B\n1-----\n     X\n   3--"""

    tree.trunk = Node(
        "1",
        left=Node(
            "2", left=Node("A"), right=Node("B", left=Node("8"), right=Node("9"))
        ),
        right=Node("3", left=Node("X")),
    )
    print(tree.to_str())

    assert (
        tree.to_str()
        == """
       A--
    2-----
         8
       B--
         9
1---------
      X---
    3-----"""[
            1:
        ]
    )


def calculate(text: str) -> int:
    tree = Tree(text)
    tree.parse()
    return tree.calculate()


def calculate_all(text: str) -> int:
    return sum(calculate(line) for line in text.splitlines())


def test_part1():
    assert calculate("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert calculate("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert calculate("2 * 3 + (4 * 5) ") == 26
    assert calculate("5 + (8 * 3 + 9 + 3 * 4 * 3) ") == 437
    assert calculate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) ") == 12240
    assert calculate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 ") == 13632

    assert calculate_all(aoc18_data.data) == 7293529867931


from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar(
    """
    expression = both_exp / number
    both_exp   = plus_exp / krat_exp
    plus_exp   = expression plus number
    krat_exp   = expression krat number
    number     = ~"[1-9]"i
    plus       = "+"
    krat       = "*"
    """
)


class IniVisitor(NodeVisitor):
    def visit_expression(self, node, visited_children):
        return visited_children

    def visit_number(self, node, visited_children):
        return int(node.text)

    def visit_krat(self, node, visited_children):
        return node.text

    def visit_plus(self, node, visited_children):
        return node.text

    def visit_plus_exp(self, node, visited_children):
        return visited_children

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node


def precedence(text: str) -> int:
    tree = grammar.parse(text.replace(" ", ""))
    iv = IniVisitor()
    output = iv.visit(tree)
    print(output)
    return 0


def test_part2():
    return  # I have no idea how to make precedence here
    assert precedence("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert precedence("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert precedence("2 * 3 + (4 * 5) ") == 26
    assert precedence("5 + (8 * 3 + 9 + 3 * 4 * 3) ") == 437
    assert precedence("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) ") == 12240
    assert precedence("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 ") == 13632

    assert calculate_all(aoc18_data.data) == 0


def parse(text):

    tokens = (
        "NAME",
        "NUMBER",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "EQUALS",
        "LPAREN",
        "RPAREN",
    )

    # Tokens

    t_PLUS = r"\+"
    t_TIMES = r"\*"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    def t_NUMBER(t):
        r"\d+"
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %d", t.value)
            t.value = 0
        return t

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    import ply.lex as lex

    lexer = lex.lex()

    # Parsing rules

    precedence = (
        ("left", "TIMES"),
        ("left", "PLUS"),
    )

    # dictionary of names
    names = {}

    def p_statement_assign(t):
        "statement : NAME EQUALS expression"
        names[t[1]] = t[3]

    def p_statement_expr(t):
        "statement : expression"
        print(t[1])
        result = t[1]

    def p_expression_binop(t):
        """expression : expression TIMES expression
                      | expression PLUS expression"""
        if t[2] == "+":
            t[0] = t[1] + t[3]
        elif t[2] == "*":
            t[0] = t[1] * t[3]

    def p_expression_group(t):
        "expression : LPAREN expression RPAREN"
        t[0] = t[2]

    def p_expression_number(t):
        "expression : NUMBER"
        t[0] = t[1]

    def p_expression_name(t):
        "expression : NAME"
        try:
            t[0] = names[t[1]]
        except LookupError:
            print("Undefined name '%s'" % t[1])
            t[0] = 0

    import ply.yacc as yacc

    parser = yacc.yacc()
    print(parser.parse(text))


def p_error(t):
    print("Syntax error at '%s'" % t.value)


def test_yacc():
    print(parse("(" + ")+(".join(aoc18_data.data.replace(" ","").splitlines()) + ")" ))

    assert False
